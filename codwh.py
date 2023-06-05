from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, callbacks=[
             StreamingStdOutCallbackHandler()], temperature=0.3)

loaders = [PyPDFLoader("./file1.pdf"),
           PyPDFLoader("./file2.pdf"),
           PyPDFLoader("./file3.pdf"),
           PyPDFLoader("./file4.pdf"),
           PyPDFLoader("./file5.pdf")]
documents = []
for loader in loaders:
    documents.extend(loader.load())
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(
    llm, vectorstore.as_retriever(), memory=memory)

while True:
    user_input = input("HUMAN: ")
    if user_input == "END":
        break
    print("AI: ", end=" ")
    qa({"question": user_input})
    print('\n')

# query = "What are the contradictions in Adi Ruppin's testimony?"
# result = qa({"question": query})
# print(result)
# query = "What was his main argument?"
# result = qa({"question": query})
# print(result)
