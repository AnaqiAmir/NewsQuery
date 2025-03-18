import time

from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain


load_dotenv()

# Initialize llm
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=500)

# Format UI
st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")
urls = []

for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
placeholder = st.empty()

query = st.text_input("Question")

# Run process when url is clicked
if process_url_clicked:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)
    placeholder.text("Loading data from URLs...")
    data = loader.load()

    # Split data into chunks
    splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "."])
    placeholder.text("Splitting documents into chunks...")
    chunks = splitter.split_documents(data)

    # Embed the chunks and store in FAISS index
    embeddings = OpenAIEmbeddings()
    placeholder.text("Storing chunks into FAISS index...")
    index = FAISS.from_documents(chunks, embeddings)

    # Retrieve QA
    start = time.perf_counter()
    placeholder.text("Initializing answering agent...")
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm, retriever=index.as_retriever()
    )
    placeholder.text("Getting answer using sources...")
    result = chain({"question": query}, return_only_outputs=True)
    end = time.perf_counter()
    placeholder.text(f"Time to retrieve answer: {round(end-start,2 )} seconds.")

    # Answers formatting
    st.subheader("Answer")
    st.write(result["answer"])

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.write(source)
