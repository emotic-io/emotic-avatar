import streamlit as st
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry, RunContext

st.title('Emotic Avatar')
st.html("<br/>")

col1,col2=st.columns([1,1])
with col1:
    st.camera_input("camera in")
with col2   :
    st.text("Meet Catoshi")
    st.image("img/Catoshi_0.jpeg",width=240)
st.audio_input("Audio In")
st.button("start streaming")



