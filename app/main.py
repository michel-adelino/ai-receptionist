import streamlit as st
from elevenlabs import generate, play
from elevenlabs import set_api_key
from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
import whisper
from st_custom_components import st_audiorec
import streamlit as st
import pandas as pd
from itertools import chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.document_loaders import DataFrameLoader
import tempfile
from streamlit_chat import message
import time

user_api_key = "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"
set_api_key("02846be0f404ef1da07358a4c1acdf35")
# Set the cache timeout in seconds (30 minutes)
CACHE_TIMEOUT = 30 * 60

@st.cache_resource(ttl=CACHE_TIMEOUT)
def load_whisper_model():
    return whisper.load_model("base")

# Load the whisper model
if not hasattr(load_whisper_model, "cache"):
    model = load_whisper_model()
else:
    model = load_whisper_model.cache

embeddings = OpenAIEmbeddings(openai_api_key=user_api_key)
vectors = FAISS.load_local("new_faiss_index", embeddings)
chain1 = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(temperature=0.0, model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
    retriever=vectors.as_retriever())

def conversational_chat(query):
    result = chain1({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]

if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello ! Ask me anything 🤗"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey ! 👋"]

def transcribe_audio(wav_audio_data):
        if wav_audio_data is not None:
            st.sidebar.success("Transcribing Audio")
            transcription = model.transcribe("../../Downloads/streamlit_audio.wav")
            st.sidebar.success("Transcription Complete")
            response = transcription["text"]
            os.remove('../../Downloads/streamlit_audio.wav')
            st.text(response)
            return response
        else:
            st.sidebar.error("Please Record Before Transcribing")


def main():
    st.title("Systems AI Receptionist")

    st.write("Would you like to proceed in text or in speech?")

    option = st.radio("Choose an option:", ("Text", "Speech"))

    if option == "Text":
        st.write("You chose to proceed in text.")

        question = st.text_input("What question would you like to ask?")

        if st.button("Get Answer"):
            if question.strip() == "":
                st.error("Please enter a question.")
            else:
                answer = conversational_chat(question)
                st.session_state['past'].append(question)
                st.session_state['generated'].append(answer)
                if len(answer) > 0:
                    st.success(answer)  # Display text answer
                    audio = generate(text=answer, voice="Bella", model="eleven_monolingual_v1")
                    play(audio)  # Play speech answer
                else:
                    st.warning("No answer found.")

    elif option == "Speech":
        st.write("You chose to proceed in speech.")         
    
        wav_audio_data, raw_audio_data = st_audiorec()
        if wav_audio_data is not None:
    # display audio data as received on the backend
            st.audio(wav_audio_data, format='audio/wav')
        st.text("Whisper Model Loaded")
        response = ""
        if st.sidebar.button("Get Answer"):
            response = transcribe_audio(wav_audio_data)

            if response.strip() == "":
                st.error(response)
                st.error("Please enter a question.")
            else:
                answer = conversational_chat(response)
                st.session_state['past'].append(response)
                st.session_state['generated'].append(answer)
                if len(answer) > 0:
                    st.success(answer)  # Display text answer
                    audio = generate(text=answer, voice="Bella", model="eleven_monolingual_v1")
                    play(audio)  # Play speech answer
                else:
                    st.warning("No answer found.")

if __name__ == "__main__":
    main()
