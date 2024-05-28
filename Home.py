##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##HuberMind[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
# Importing dependencies
import streamlit as st
from pathlib import Path
import base64
import sys
import os
import logging
import warnings
from dotenv import load_dotenv
from typing import Any, Dict
import google.generativeai as genai
from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
from crewai import Crew, Process, Agent, Task
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
from fpdf import FPDF
#Importing from SRC
from crewai import Crew, Process, Agent, Task
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
from fpdf import FPDF
#Importing from SRC
# from src.crews.agents import researcher, insight_researcher, writer, formater
# from src.crews.task import research_task, insights_task, writer_task, format_task
# from src.crews.crew import botimus_crew
from src.components.navigation import footer, custom_style, page_config
##################################################################################################
##################################################################################################
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
##################################################################################################
##################################################################################################
#Environmental variables For developing and testing
# load_dotenv()
# google_api_key = os.getenv("GOOGLE_API_KEY")
##################################################################################################
##################################################################################################

#Check if api key loaded successfully with logging info For developing and testing
# if google_api_key:
#     logger.info("Google API Key loaded successfully.")
# else:
#     logger.error("Failed to load Google API Key.")
##################################################################################################
#Intializing llm
page_config("HuberMind", "🤖", "wide")
custom_style()
st.sidebar.image('./src/logo.png')
google_api_key = st.sidebar.text_input("Enter your GeminiPro API key:", type="password")

llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, 
                             temperature=0.2, google_api_key=google_api_key)


##################################################################################################


# Custom Handler for logging interactions
class CustomHandler(BaseCallbackHandler):
    def __init__(self, agent_name: str) -> None:
        super().__init__()
        self.agent_name = agent_name

    def on_chain_start(self, serialized: Dict[str, Any], outputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": "assistant", "content": outputs['input']})
        st.chat_message("assistant").write(outputs['input'])

    def on_agent_action(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": "assistant", "content": inputs['input']})
        st.chat_message("assistant").write(inputs['input'])

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": self.agent_name, "content": outputs['output']})
        st.chat_message(self.agent_name).write(outputs['output'])
        
        
# def generate_pdf(text):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=text, ln=True, align='C')
#     return pdf.output(dest='S').encode('latin-1')

# Main function to run the Streamlit app
def main():
    st.title("🧠HuberMind🧠")
    st.markdown('''
            <style>
                div.block-container{padding-top:0px;}
                font-family: 'Roboto', sans-serif; /* Add Roboto font */
                color: blue; /* Make the text blue */
            </style>
                ''',
            unsafe_allow_html=True)
    st.markdown(
        """
        ### A Andrew Hyberman's Youtbe Videos Blog Generated with AI Agents, powered by Gemini, CrewAI & [Towards-GenAI](https://github.com/towards-genai)
        """
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    col1, col2 = st.columns(2)
    # Input for blog topic
    with col1:
        blog_topic = st.text_input("Enter the blog topic:")

    # Dropdown for selecting the type of content
    with col2:
        
        content_type = st.selectbox("Select the type of content:", ["Blog Post", "Research Paper", "Technical Report"])

    

    # Button to start the task execution
    if st.button("Start Blogging Crew"):
        if blog_topic:
            # result = tech_crew.kickoff()
            result="Test"
            st.write(result)
            
            # Create a PDF and write the output to it
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for line in result.split("\n"):
                pdf.write(5, line)
                pdf.ln()  # move to next line

            # Save the PDF file
            pdf.output("blog.pdf")
            file_path = './blog.pdf'
            with open(file_path, 'rb') as file:
                file_content = file.read()

            # Create download button
            st.download_button(
                label="Download blog.pdf",
                data=file_content,
                file_name="blog.pdf",
                mime="application/pdf"
            )
                
            
        else:
            st.error("Please enter a blog topic.")
            
    

if __name__ == "__main__":
    main()
    with st.sidebar:
        
        footer()
        
        
        
        