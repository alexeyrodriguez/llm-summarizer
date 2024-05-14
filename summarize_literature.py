import arxiv
import yaml
import os
import os.path
from dataclasses import dataclass
import re
import pypdf
from llm_utils import OpenAIClient, SummarySpec
from prompts import all_specs


@dataclass
class Paper:
    title: str
    filename: str
    dirname: str

def load_papers():
    with open('literature/tts.yaml') as f:
        lit = yaml.safe_load(f)

    os.makedirs('papers', exist_ok=True)

    papers = []
    for arxiv_id in lit['arxiv_ids']:
        paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
        paper_name = f'papers/{arxiv_id}.pdf'

        papers.append(Paper(paper.title, paper_name, re.sub("[^a-zA-Z]+", "_", paper.title)))

        if not os.path.exists(paper_name):
            print('Downloading paper:', arxiv_id, paper.title)
            paper.download_pdf(filename=paper_name)
    return papers

def summarize_paper(client: OpenAIClient, summary_spec: SummarySpec, paper: Paper) -> None:
    reader = pypdf.PdfReader(paper.filename)
    pages = [p.extract_text() for p in reader.pages]
    answer, summ_prompt = client.run_summary(summary_spec, pages)
    os.makedirs(f"summaries/{paper.dirname}", exist_ok=True)
    os.makedirs(f"summaries/{paper.dirname}/logs", exist_ok=True)

    with open(f"summaries/{paper.dirname}/{summary_spec.fname}.txt", "w") as f:
        f.write(answer)

    with open(f"summaries/{paper.dirname}/logs/{summary_spec.fname}.txt", "w") as f:
        f.write(summ_prompt)


client = OpenAIClient()
papers = load_papers()
for paper in papers:
    for spec in all_specs:
        summarize_paper(client, spec, paper)
