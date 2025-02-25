from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

system_prompt = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain =  prompt_template | model | parser

api = FastAPI(
    title="Simple Translator",
    version="0.0.1"
)
add_routes(api, chain, path="/translator")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="localhost", port = 8080)
