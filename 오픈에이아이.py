import streamlit as st
import os
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = st.secrets['api_key']

st.title("이미지 생성기입니다.")

with st.form("form"):
    user_input = st.text_input("뭐 그릴래?")
    size = st.selectbox("size",['1024x1024', '512x512', '256x256'])
    submit = st.form_submit_button("submit")


if submit and user_input:
    gpt_prompt = [{'role': 'system', 
               'content': 'Imagine the detail appeareance of the input.Response it shortly around 15 words'}]

    gpt_prompt.append(
    {'role': 'user', 'content': user_input}
    )

    client = OpenAI()
    with st.spinner("Waiting for chatGPT ..."):
        response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages = gpt_prompt
        )

        st.write(gpt_prompt)


        st.write("dall-e prompt:", response.choices[0].message.content)
        dall_e_prompt = response.choices[0].message.content

        dall_e_response = client.images.generate(
        model='dall-e-3', prompt = dall_e_prompt,
        size = '1024x1024'
        )

        st.image(dall_e_response.data[0].url)
    








