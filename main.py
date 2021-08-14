# Imports adicionais #
import pyttsx3 as tts
import speech_recognition as sr
import sys

# Imports obrigatórios #
from vosk import Model, KaldiRecognizer
import pyaudio
import os

# Preparando modelo (Base de reconhecimento) e reconhecedor #
model = Model("models")
rec = KaldiRecognizer(model, 16000)

# Configurando propriedades do microfone de captura #
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Ouvindo #
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())