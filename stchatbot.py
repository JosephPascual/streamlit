from openai import OpenAI
import tiktoken
import json
from datetime import datetime
import os
import streamlit as st

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
DEFAULT_TOKEN_BUDGET = 4096

# Classes
class ConverstaionManager:
    def __init__(self):
        return None
    
    def set_persona(self):
        # Adjust the chatbot's personality
        return None

    def set_custom_system_message(self):
        # Allows users to set a customer system message
        return None
    
    def chat_completion(self):
        # Generates responses based on user input
        return None

    def reset_conversation_history(self):
        # Clears chat history
        return None
        
        
# Working Code Below

st.title("Joe's Chatbot")