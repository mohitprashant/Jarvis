# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:26:37 2025

@author: 18moh
"""

from RealtimeSTT import AudioToTextRecorder
import datetime

def process_text(text):
    print(text)
    
def start_callback():
    print("Recording started!")

def stop_callback():
    print("Recording stopped!")

if __name__ == '__main__':
    recorder = AudioToTextRecorder()
    
    time_start = datetime.datetime.now()
    while (datetime.datetime.now() - time_start).total_seconds() < 10:
        recorder.text(process_text)
        
    recorder.shutdown()