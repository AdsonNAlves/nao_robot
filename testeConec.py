import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound

def audio_recording():
    # obtain audio from the microphone
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        # print("Diga algo!")
        # playsound('/media/ic-unicamp/adson_ext1/adson/Trabalho/Inovacao/asambox/speechrecognition/apresent.mp3')
        # time.sleep(5)
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        texto =r.recognize_google(audio, language='pt-BR')
        print(texto)
        if str(texto).lower() in 'parar' or str(texto).lower() in 'desligar':
            print('Até Logo')
            return 0
        if str(texto).lower() in 'gravar':
            print('Estou gravando')
            with sr.Microphone() as source:
                gravacao = r.listen(source)
            txgrav =r.recognize_google(gravacao, language='pt-BR')
            rec=gTTS(txgrav, lang='pt-br')
            rec.save('/media/ic-unicamp/adson_ext1/adson/Trabalho/Inovacao/asambox/speechrecognition/rec.mp3')
            print('Gravado- Ira ouvir quando desligar!')
            return 1
        else:
            return 1
    except sr.UnknownValueError:
        print("Não entendi o audio")
        return 1
    except sr.RequestError as e:
        print("Nenhum resultado da requisição; {0}".format(e))
        return 1

    #time.sleep(0.5)
    
action=1
while action:
    action = audio_recording()
    if action == 0:
        playsound('/media/ic-unicamp/adson_ext1/adson/Trabalho/Inovacao/asambox/speechrecognition/rec.mp3')