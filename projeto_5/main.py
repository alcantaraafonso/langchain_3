from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

db = SQLDatabase.from_uri("sqlite://chinook.db")

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.0, # quanto mais próximo de 1, mais criativo
    openai_api_key=openai_api_key,
    verbose=True
)

# db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# db_chain.run("How many albuns are there?")


agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run("How many albuns are there?")