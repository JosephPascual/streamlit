from together import Together
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

class ConversationManager:
    def __init__(self, api_key=None, base_url=None, model=None, temperature=None, max_tokens=None, token_budget=None):
        if not api_key:
            api_key = DEFAULT_API_KEY
        if not base_url:
            base_url = DEFAULT_BASE_URL
            
        self.client = Together(
            api_key=api_key,
            base_url=base_url
        )


        self.model = model if model else DEFAULT_MODEL
        self.temperature = temperature if temperature else DEFAULT_TEMPERATURE
        self.max_tokens = max_tokens if max_tokens else DEFAULT_MAX_TOKENS
        self.token_budget = token_budget if token_budget else DEFAULT_TOKEN_BUDGET
        self.system_messages = {
            "blogger": "You are a creative blogger specializing in engaging and informative content for GlobalJava Roasters.",
            "social_media_expert": "You are a social media expert, crafting catchy and shareable posts for GlobalJava Roasters.",
            "creative_assistant": "You are a creative assistant skilled in crafting engaging marketing content for GlobalJava Roasters.",
            "custom": "Enter your custom system message here."
        }
        self.system_message = self.system_messages["creative_assistant"]  # Default persona
        self.conversation_history = [{"role": "system", "content": self.system_message}]

    def chat_completion(self, prompt, temperature=None, max_tokens=None):
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens
        # Append the user's prompt to conversation_history
        self.conversation_history.append({"role": "user", "content": prompt})
        self.enforce_token_budget()

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as e:
            print(f"An error occured with self.client.chat.completions.create(): {e}")
            return None
        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})

        return ai_response
    
    def count_tokens(self, text):
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(text)
        return len(tokens)
    
    def total_tokens_used(self):
        return sum(self.count_tokens(message['content']) for message in self.conversation_history)
    
    def enforce_token_budget(self):
        while self.total_tokens_used() > self.token_budget:
            if len(self.conversation_history) <= 1:
                break
            self.conversation_history.pop(1)

    def set_persona(self, persona):
        if persona in self.system_messages:
            self.system_message = self.system_messages[persona]
            self.update_system_message_in_history()
        else:
            raise ValueError(f"Unknown persona: {persona}. Available personas are: {list(self.system_messages.keys())}")
    
    def set_custom_system_message(self, custom_message):
        if not custom_message:
            raise ValueError("Custom message cannot be empty.")
        self.system_messages['custom'] = custom_message
        self.set_persona('custom')
    
    def update_system_message_in_history(self):
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            self.conversation_history[0]["content"] = self.system_message
        else:
            self.conversation_history.insert(0, {"role": "system", "content": self.system_message})
       
    def reset_conversation_history(self):
        try:
            self.conversation_history = [{"role": "system", "content": self.system_message}]  # Attempt to save the reset history to the file
        except Exception as e:
            print(f"An unexpected error occurred while resetting the conversation history: {e}")

        
# Working Code Below

if 'chat_manager' not in st.session_state:
    st.session_state['chat_manager'] = ConversationManager()
    
cm = st.session_state['chat_manager']

st.title("Joe's Chatbot")

