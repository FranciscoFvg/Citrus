import pyttsx3 as tts
import speech_recognition as sr
import sys
import time

#Config's
engine = tts.init()
engine.setProperty('voice', 0)


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()
    frase = ''

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except Exception as e:
        print("\033[1;31mNão entendi. Erro: ", e)

    return frase

aname = 'citrus'

#Execução
while True:
    print('\033[m')
    texto = ouvir_microfone()
    texto = texto.lower()
    if aname in texto:
        ordem = texto[(len(aname)+1):]
        ordem = ordem.lower()

        if 'desligar' in ordem:
            print(ordem)
            engine.say('Desligando assistente virtual!')
            engine.runAndWait()
            sys.exit()
        print(ordem)
        engine.say(ordem)
        engine.runAndWait()
    else:
        print('sem correpondencia')