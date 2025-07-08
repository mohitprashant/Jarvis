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
        self.buffer = []
        self.skill_list = []
        self.persona = ''
        
        try:
            self.client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
                )
        except:
            print("LLM Not Available")
            
        self.reset_buffer()
        
        
        
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
        return chat_completion.choices[0].message.content
    
    
    
    def chained_prompt(self, content, role='user'):
        self.buffer.append({'role' : role, 'content' : content})
        chat_completion = self.client.chat.completions.create(
            messages=self.buffer,
            model= self.model,
        )
        return chat_completion.choices[0].message.content
    
    
    
    def interaction(self, content, role="user"):
        print('\nInput: ', content , '\n', flush=True)
        out = self.chained_prompt(content)
        print('\nAgent: ', out, '\n', flush=True)
        # self.buffer.append({'role' : role, 'content' : content})
        self.buffer.append({'role': 'assistant', 'content' : out})
        
        
        
    def reset_buffer(self):
        self.buffer = [{"role" : "system", "content" : self.persona}]



    def load_skill_list(self, skill_file):
        with open(skill_file) as f:
            for x in f:
                self.skill_list.append(x)
                
 
                
    def load_persona(self, persona_file):
        self.persona = ''
        with open(persona_file) as f:
            for x in f:
                self.persona += x + '\n'
                
        self.persona += "Do not say more than 100 words unless asked to elaborate. \n"
        self.persona += "\n\nYou also have the following skills: \n - kindness\n"
        for x in self.skill_list:
            self.persona += " - " + x
            
        self.reset_buffer()
            
        
        


if __name__ == '__main__':
    agent = LLMHandler()
    print(agent.single_prompt("Give me recent news from this month"))
