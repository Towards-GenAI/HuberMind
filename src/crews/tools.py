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




##################################################################################################
#Using only inbuilt CrewAI tools for HuberMind

#YT Channel Search tool
from crewai_tools import YoutubeChannelSearchTool

#Initialize the tool with a specific Youtube channel handle to target your search
yt_channel_sreach_tool = YoutubeChannelSearchTool(youtube_channel_handle='@hubermanlab')
##################################################################################################
#YT search tool
from crewai_tools import YoutubeVideoSearchTool

video_url=[]
video_search_tool = YoutubeVideoSearchTool(youtube_video_url=video_url)
##################################################################################################
# Serper tool
from crewai_tools import SerperDevTool
load_dotenv()
serper_api_key = os.getenv("SERPER_API_KEY")
serper_tool = SerperDevTool(serper_api_key=serper_api_key, verbose=True)
##################################################################################################

#PDF RAG tool

# Initialize the tool allowing for any PDF content search if the path is provided during execution
from crewai_tools import PDFSearchTool
pdf_path=[]
pdf_tool = PDFSearchTool(pdf=pdf_path)
##################################################################################################















