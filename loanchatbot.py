import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    if os.path.exists('faiss_index'):
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
   


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):  
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings=embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    
    return response["output_text"]
def app():
    pdf_docs=['Home Loan Information.pdf']
    if os.path.isdir('faiss_index')==False:
        raw_text = get_pdf_text(pdf_docs)
        text_chunk=get_text_chunks(raw_text)

        get_vector_store(text_chunk)


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        initial_message = AIMessage("Hi, how can I help you?")
        st.session_state.chat_history.append(initial_message)

    st.title('Insurance ChatBot')

    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message('Human'):
                st.markdown(message.content)
        else:
            with st.chat_message('AI'):
                st.markdown(message.content)

    user_query = st.chat_input('Your message')
    if user_query:
        st.session_state.chat_history.append(HumanMessage(user_query))
        with st.chat_message('Human'):
            st.markdown(user_query)

        ai_response = user_input(user_query)
        with st.chat_message('AI'):
            st.markdown(ai_response)

        st.session_state.chat_history.append(AIMessage(ai_response))

if __name__ == '__main__':
    app()