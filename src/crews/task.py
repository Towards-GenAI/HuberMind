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










##################################################################################################

#fomat the text in markdown with clear headline and paragraphes
## Research Task
research_task = Task(
  description=
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
    "Get data like views, likes, comments, duration, description etc."
  ,
  expected_output='A comprehensive 5 paragraphs long report based on the {topic} of video content.',
  tools=[serper_tool],
  agent=channel_researcher
)

# Writing task with language model configuration
write_task = Task(
  description=
    "get the info from the youtube channel on the topic {topic}."
  ,
  expected_output='Summarize the info from the Huberman youtube channel video on the topic{topic} and create the content for the blog',
  tools=[serper_tool],
  agent=blog_writer,
  async_execution=False,

)


# Editor & Translator
edit_translate_task = Task(
  description=
    "Edit the blog and Transalte in French on {topic}."
  ,
  expected_output='Edit the blog writen Huberman youtube channel video on the topic{topic} and create the content for the blog in French to',
  tools=[serper_tool],
  agent=blog_rewiewer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)