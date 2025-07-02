# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:46:11 2025

@author: 18moh
"""

import os
from groq import Groq


class LLMHandler(self):
    def __init__(self):
        self.client = None
        
        try:
            self.client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
                )
        except:
            print("LLM Not Available")
        
        
    def prompt(self):
        
            
    
    



chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

