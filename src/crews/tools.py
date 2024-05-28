##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##HuberMind[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import streamlit as st
from pathlib import Path
import base64
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from crewai import Crew, Process, Agent, Task
from langchain_core.callbacks import BaseCallbackHandler
from typing import TYPE_CHECKING, Any, Dict, Optional
from langchain_openai import ChatOpenAI
import logging
import warnings
warnings.filterwarnings('ignore')
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
import logging

##################################################################################################
#Environmental variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
##################################################################################################
##################################################################################################

#Check if api key loaded successfully with logging info
# if google_api_key:
#     logger.info("Google API Key loaded successfully.")
# else:
#     logger.error("Failed to load Google API Key.")
# ##################################################################################################
#Intializing llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, 
                             temperature=0.2, google_api_key=google_api_key)

llm_flash=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.2,
                           google_api_key=google_api_key)

llm = {
    # Assuming 'llm' expects certain keys and values, fill them accordingly
    'verbose': True,
    'model': 'gemini-pro',
    'client': {
        'model_name': 'models/gemini-pro',
        'generation_config': {},
        'safety_settings': {}
    },
    'google_api_key': google_api_key,
    'temperature': 0.2
}
##################################################################################################

##################################################################################################
#Using only inbuilt CrewAI tools for HuberMind

#YT Channel Search tool
from crewai_tools import YoutubeChannelSearchTool

#Initialize the tool with a specific Youtube channel handle to target your search
# yt_channel_sreach_tool = YoutubeChannelSearchTool(youtube_channel_handle='@hubermanlab', llm=llm)
##################################################################################################
#YT search tool
from crewai_tools import YoutubeVideoSearchTool

video_url=[]
# video_search_tool = YoutubeVideoSearchTool(youtube_video_url=video_url,llm=llm)
##################################################################################################
# Serper tool
from crewai_tools import SerperDevTool
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
serper_tool = SerperDevTool( verbose=True)
##################################################################################################

#PDF RAG tool

# Initialize the tool allowing for any PDF content search if the path is provided during execution
from crewai_tools import PDFSearchTool
pdf_path=[]
# pdf_tool = PDFSearchTool(pdf=pdf_path, llm=llm)
##################################################################################################















