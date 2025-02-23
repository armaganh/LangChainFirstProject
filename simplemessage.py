from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

messages = [
    SystemMessage(content="Translate the following from English into Spanish"),
    HumanMessage(content="hi!"),
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)
    print(response.content)