# Using different models with LangChain
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

def run_myscript():
  question = "Who won the FIFA World Cup in the year 1994? "
  
  template = """Question: {question}
  
  Answer: Let's think step by step."""
  
  prompt = PromptTemplate(template=template, input_variables=["question"])
  
  repo_id = "google/flan-t5-xxl"  
  
  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
  
  llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs={"temperature": 0.1, "max_length": 64}
  )
  llm_chain = LLMChain(prompt=prompt, llm=llm)
  
  print(llm_chain.run(question))


