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
        except:
            print("LLM Not Available")
        
        
    def single_prompt(self, content, role="user"):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": role,
                    "content": content,
                }
            ],
            model= self.model,
        )
        
        return self.client.chat_completion.choices[0].message.content


if __name__ == '__main__':
    
    agent = LLMHandler()
    print(agent.single_prompt("Tell me your purpose"))
