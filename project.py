from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

loader1 = PyPDFLoader("./file1.pdf")
loader2 = PyPDFLoader("./file2.pdf")
loader3 = PyPDFLoader("./file3.pdf")
loader4 = PyPDFLoader("./file4.pdf")
loader5 = PyPDFLoader("./file5.pdf")

index = VectorstoreIndexCreator().from_loaders(
    [loader1, loader2, loader3, loader4, loader5])

query = "What are the contradictions in Adi Ruppin's testimony?"
print(index.query(query))
query = "What are the contradictions in Adi Ruppin's statements?"
print(index.query(query))
query = "What are the main issues Elad Rave has raised?"
print(index.query(query))
