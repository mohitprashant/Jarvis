# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 02:39:07 2025

@author: 18moh
"""
import torch
from TTS.api import TTS


if __name__ == '__main__':
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(device)
    
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    wav = tts.tts(text="Hello world.", speaker_wav="Internal Data/Ego/accent.wav", language="en")