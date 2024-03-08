import streamlit as st
from streamlit.logger import get_logger
from textblob import TextBlob
import google.generativeai as genai


LOGGER = get_logger(__name__)


def run():
  st.set_page_config(
        page_title="Power of LLMs",
        page_icon="💻",
    )

  genai.configure(api_key=st.secrets["API_KEY"])

  model = genai.GenerativeModel('gemini-pro')

  #st.write(model.generate_content("whats ur name").text)



  st.write("Neel Iyer | MSEC Power of LLMs")
  st.write("We explore the possibility of using large language models (LLMs) to reduce media subjectivity. Please input a demo article or piece of text below (Errors are likely due to harmful, inappropriate, or excessively long text inputs): ")

  prompt = st.chat_input("Say something")
  if prompt:
      st.write(f"Article Inputted: {prompt}")
      st.write(f"Article Subjectivity (0.0-1.0):  {TextBlob(prompt).sentiment.subjectivity}")
      prompt2 = "rewrite the following text to be concise, fact driven, objective, neutral statements that aren't lengthy. they shouldnt hold any political affiliation but be fact driven and short. u should have a formal, neutral tone and not express any one view but present both sides equally and fairly: "
      response = model.generate_content(prompt2 + prompt)
      st.write(f"Rewritten Article: {response.text}")
      st.write(f"Rewritten Article Subjectivity (0.0-1.0): {TextBlob(response.text).sentiment.subjectivity}" )

if __name__ == "__main__":
    run()
