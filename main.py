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



if __name__ == '__main__':
    recorder = voc.AudioToTextRecorder()
    agent = llm.LLMHandler()
    
    
    time_start = datetime.datetime.now()
    while (datetime.datetime.now() - time_start).total_seconds() < 10:
        recorder.text(agent.interaction)
        
    recorder.shutdown()
    