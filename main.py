# Imports adicionais #
import speech_recognition as sr
import sys

# Imports obrigatórios #
from vosk import Model, KaldiRecognizer
import pyttsx3 as tts
import pyaudio
import json
import os

# Inicializando Componentes de Síntese#
engine = tts.init()
engine.setProperty('voice', 0)

# Função de Síntese de Voz #
def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            speak(text)
