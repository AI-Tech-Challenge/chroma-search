import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(",")

chat_model = ChatOpenAI(temperature=0.5)

system_template = """You are a helpful assistant who generates comma separated lists.
A user will pass in an input, and you should generate 3 color hex codes that fit that input in a comma separated list.
ONLY return a comma separated list, and nothing more.
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chain = LLMChain(
    llm = chat_model,
    prompt = chat_prompt,
    output_parser = CommaSeparatedListOutputParser(),
)

def generate_hexcodes(input):
    return chain.run(input)

