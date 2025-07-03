# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:46:11 2025

@author: 18moh
"""

import os
from groq import Groq


class LLMHandler():
    def __init__(self):
        self.client = None
        self.model = "llama-3.3-70b-versatile"
        
        try:
            self.client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
                )
            return True
        except:
            print("LLM Not Available")
            return False
        
        
    def single_prompt(self, content, role="user"):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": role,
                    "content": content,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        return chat_completion.choices[0].message.content

