- add the case pdf files into a google drive folder.
- take folder ID and use it to load the files into LLM memory
- ask questions about the contents of the files

Project: We want ChatGPT to access files in google drive and be able to answer questions related to those files.
What we need:
- OpenAI API: to use ChatGPT.
- LangChain: To write the code that will be used.
- Google Drive API: to access the files in Google Drive for the LLM to use.

Approach:
- firstly we would need to understand how to load data into LLM conversation memory or in other words,
  give it some context, to do this we write a small text file with some information and then find out how to
  use LangChain and other tools and libraries to use this context.
- secondly we need to access the Google Drive files and get the data in them using an API so we can use method 1
  to accomplish the task.
- Finally we could connect the 2 solutions to form the solution for our main problem. (answering queries 
  related to Google Drive files)

Tools:
- LangChain document loaders: this allows us to use loaders for different file formats and load the data in them.
- OpenAI: this allows us to use the OpenAI library along with the OpenAI API
- Google Drive API: this allows us to do calls and retrieval of files from the Google Drive.
- VectorstoreIndexCreator: to allows us to use loaders (of different types) to add them to the LLM memory and 
  to the query "context"

Steps:
- firstly I wanted to start small and load the data from a local text file into the query "context",
  thus I used TextLoader funstion to create a simple loader which I used with the VectorstoreIndex to apply
  the data to the query "context". This worked out and the LLM was able to answer questions with the use
  of the data in the text file.
- secondly I wanted to attempt this with a PDF file, so I searched for multiple PDF loaders, I tried multiple
  the one from LlamaIndex didn't work. I was able to load the contents of a local PDF file and use queries
  on that data successfully. 
- thirdly I wanted to access files on my Google Drive and not locally, I signed up to the Google Drive API and 
  searched on how to use it, I wrote code to load and print the contents of a file on Google Drive, to ensure
  it worked with other people's files on Google Drive I used a link my friend gave me to access a file
  on his Google Drive. I was able to use a loader on a Google Drive file that is not local.
- Finally I integrated the google drive loader into the program that used the simple text loader and tested it,
  I used my CV on google drive as well as other documents and it worked. I was able to complete the task.

What I learned:
- I learned how to use loaders, how to create query "context", how to create conversation memory(didn't help
  me with the task) and how to use third party APIs along with LangChain to write my program.














