# Machine Learning Paper Summarizer

This is a summarizer for machine learning papers based on LLMs.
Currently it uses OpenAI's APIs but it should be easy to adapt to use other APIs or locally running LLMs.

The approach is simple, there are summaries for different aspects of the paper (e.g. training, preprocessing, etc),
for each aspect, first the relevant information is extracted from each page of the paper, and in a subsequent pass all
this collected information is used to make an overall summmary.

The generated summaries for a few selected Text to Speech papers are in the summaries directory.
