from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
chat = ChatOpenAI(temperature=0.9)


conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

# response = conversation.run(
#     "Answer briefly. What are the first 3 colors of a rainbow?")
# print(response)
# response = conversation.run("And the next 4?")
# print(response)

while True:
    user_input = input(">")
    if user_input == "END":
        break
    response = conversation.run(user_input)
    print("AI: ", response)
