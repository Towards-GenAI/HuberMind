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
from src.crews.tools import *



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





# Creating a senior researcher agent with memory and verbose mode

channel_researcher=Agent(
    role="Senior Researcher for Youtube channels",
    goal='get the relevant video transcription for the topic {topic} from the provided Huberman youtbe channel channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in Neural, Mind, Dopamine, Adhd and psychology of mind and providing suggestion" 
    ),
    tools=[serper_tool],
    allow_delegation=True, llm=llm
  )
   



blog_writer=Agent(
    role='Blog Writer based on youtbe vidoe transcript',
    goal='Narrate compelling research stories about the video {topic} from Huberman youtbe channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
        "Write in a clear and concise manner."
        "Tone should be friendly, funny, and engaging with attention to details"
    ),
    tools=[serper_tool],
    allow_delegation=True,llm=llm


)

blog_rewiewer=Agent(
    role='Blog rewiewer based on blo wrtten',
    goal='rewiewer the blog written on {topic} from Huberman youtbe channel, in professional style',
    verbose=True,
    memory=True,
    backstory=(
        "rewiewer the blog in NY times style"
        "rewiewer the blog in professional style to match according to {topic} in Huberman youtbe channel"
        "translate into French and write below English version of the blog"
    ),
    tools=[serper_tool],
    allow_delegation=False,llm=llm


)