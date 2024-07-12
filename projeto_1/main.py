from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def generate_company_name():
    llm = ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, # quanto mais próximo de 1, mais criativo
        openai_api_key=openai_api_key
    )

    '''
    SystemMessage e HumanMessage abstraem a role que o ChatGPT recebe
    messages = [
        {
            "role": "system", 
            "content": "Your responses should not exceed five sentences in length."
        },
        {
            "role": "user", 
            "content": user_prompt
        } 
    ]
    '''
    company_name = llm(
        [
            SystemMessage(
                content='você é um assistante IA que sempre response em Português do Brasil'
            ),
            HumanMessage(
                content='Gere 5 ideias de nomes para empresas no segmento de Pets'
            )
        ]
    )

    return company_name

if __name__ == '__main__':
    print(generate_company_name())