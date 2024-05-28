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
#Importing from SRC
from src.crews.agents import *
from src.crews.task import *



##################################################################################################
##################################################################################################
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
##################################################################################################
##################################################################################################
#Environmental variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
##################################################################################################
##################################################################################################

#Check if api key loaded successfully with logging info
if google_api_key:
    logger.info("Google API Key loaded successfully.")
else:
    logger.error("Failed to load Google API Key.")
##################################################################################################
#Intializing llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, 
                             temperature=0.2, google_api_key=google_api_key)

llm_flash=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.2,
                           google_api_key=google_api_key)


##################################################################################################


#HuberMin crew #1

huber_crew=Crew(
  agents=[channel_researcher, blog_writer, blog_rewiewer],
  tasks=[research_task, write_task, edit_translate_task],
  process=Process.sequential,  # Tasks will be executed one after the other
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=huber_crew.kickoff(inputs={'topic':'Dr. Matt Walker: Using Sleep to Improve Learning, Creativity & Memory | Huberman Lab Guest Series'})




