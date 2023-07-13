from langchain import PromptTemplate
from langchain import HuggingFaceHub, LLMChain
import os


template = """Question: {question}
Answer: """

prompt = PromptTemplate(template=template,input_variables=['question'])
question = "Which NFL team won the super bowl in the 2010 season?"

os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'HF_API_KEY'

# initialize Hub LLM
hub_llm = HuggingFaceHub(
        repo_id='google/flan-t5-xl',
    model_kwargs={'temperature':1e-10}
)

# create prompt template > LLM chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)

# ask the user question about NFL 2010
print(llm_chain.run(question))