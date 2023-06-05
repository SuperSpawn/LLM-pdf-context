from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

loader1 = PyPDFLoader("./file1.pdf")

# 0.2 so the LLM has at least some creativity
llm = OpenAI(temperature=0.7)


conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(loader1.load())
)

# conversation.predict(input="My name is Talal Zoabi")
# conversation.predict(input="What is my name?")

while True:
    user_input = input(">")
    if user_input == "END":
        break
    response = conversation.predict(input=user_input)
    print("AI: ", response)

print(conversation.memory.buffer)
