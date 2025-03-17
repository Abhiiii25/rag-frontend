import streamlit as st
import requests

API_URL_UPLOAD = "http://127.0.0.1:5000/upload"
API_URL_QUERY = "http://127.0.0.1:5000/query"

st.title("RAG Application - Document Q&A")

# File Upload Section
st.header("Upload a Document")
uploaded_file = st.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    response = requests.post(API_URL_UPLOAD, files=files)
    if response.status_code == 200:
        st.success("File uploaded and processed successfully!")
    else:
        st.error(f"Error: {response.json().get('error', 'Unknown error')}")

# Query Section
st.header("Ask a Question")
query = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if query:
        response = requests.post(API_URL_QUERY, json={"query": query})
        if response.status_code == 200:
            st.success(f"Answer: {response.json().get('response')}")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.warning("Please enter a question.")
