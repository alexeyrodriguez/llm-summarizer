from dataclasses import dataclass
from openai import OpenAI

@dataclass
class SummarySpec:
    extract_prompt: str # Prompt to run on each page of a paper, set to None to not perform an extraction
    summary_prompt: str # Prompt to run on the extracted content of each page
    fname: str
    max_pages: int = None

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI()

    def call_model(self, user_prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
        )

        # See API ref: https://platform.openai.com/docs/guides/text-generation/chat-completions-api
        return response.choices[0].message.content
    
    def extract_details(self, query, text):
        user_prompt = f"""
Please answer to the following request using the context extracted from a machine learning paper:

Request:
{query}

Context:
{text}
"""
        return self.call_model(user_prompt)

    def run_summary(self, summary_spec: SummarySpec, pages: list[str]) -> tuple[str, str]:

        if summary_spec.extract_prompt:
            res = []
            for page in enumerate(pages):
                res.append(self.extract_details(summary_spec.extract_prompt, page))
        else:
            res = pages

        summ_prompt = summary_spec.summary_prompt
        summ_prompt += "\n\nContext:\n"
        for page_num, response in enumerate(res):
            summ_prompt += f"Page {page_num}:\n{response}\n\n"

        summary = self.call_model(summ_prompt)
        return summary, summ_prompt
