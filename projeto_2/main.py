from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def generate_company_name(segmento):
    llm = ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, # quanto mais próximo de 1, mais criativo
        openai_api_key=openai_api_key
    )

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "você é um assistante IA que sempre response em Português do Brasil"
            ),
            (
                "human",
                "Gere 5 ideias de nomes para empresas no segmento de {segmento}"
            )
        ]
    )

    company_names_chain = LLMChain(
        llm=llm,
        prompt=chat_template,
        output_key="company_name"
    )

    return company_names_chain({"segmento": segmento})

if __name__ == '__main__':
    print(generate_company_name("imobiliária"))