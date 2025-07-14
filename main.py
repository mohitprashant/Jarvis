# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:20:33 2025

@author: 18moh
"""

import numpy as np
import torch
import datetime
import voice_input as voc
from voice_input import process_text
import llm_handler as llm
import os
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__maind__':
    recorder = voc.AudioToTextRecorder()
    agent = llm.LLMHandler()
    
    config = {
        'skills' : 'Internal Data/Ego/skill_list.cfg',
        'persona' : 'Internal Data/Ego/persona.cfg'
        }
    
    for x in config:
        if not os.path.exists(config[x]):
            with open(config[x], 'w') as file:
                file.write("")                                         # Temporary
                print("Config created : ", config[x])
        else:
            print("Config loaded : ", config[x])
            
    
    agent.load_skill_list(config['skills'])
    agent.load_persona(config['persona'])
    
        
    
    time_start = datetime.datetime.now()
    while((datetime.datetime.now() - time_start).total_seconds() < 10):
        recorder.text(agent.interaction)
        
    recorder.shutdown()
    
    print(agent.persona)
    print(agent.buffer)
    