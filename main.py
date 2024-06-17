import pyautogui as ptg
import speech_recognition as sr
import pywhatkit
import wikipedia
import time
from datetime import datetime
import tools


# Para estudio
import os
import sys

# import platform


# Herramientas/tools:
ptg_tools = tools.pyautogui_tools()
ptt3_tools = tools.pyttsx3_tools()
sr_tools = tools.speech_recognition_tools()

# ptg_tools.locate_pointer() Opcional para encontrar puntos especificos del puntero en pantalla


# Variables principales
Recognizer = sr_tools.create_recognizer()
current_time = datetime.now()

# Configuración de voz
ptt3_tools.set_Properties_voice()
# ptt3_tools.talk("abcdefghijklmnñopqrstuvwxyzaaaa")
# sys.exit()
#




comandos = {
    "reproduce": " Reproduce un video en youtube",
    "hola": " saluda",
    "fecha": " Indica la fecha",
    "hora": " Indica la hora",
    "busca": " Investiga información en wikipedia",
    "comandos": " Informa al usuario sobre los comandos disponibles",
}


# Métodos principales


def listen_and_transcribe():  # Recibe texto oralmente
    with sr.Microphone() as source:
        ptt3_tools.talk("Escuchando...")
        # audio = Recognizer.adjust_for_ambient_noise(source,duration=5)
        audio = Recognizer.listen(source)
        try:
            text = Recognizer.recognize_google(audio, language="es-ES")
        except sr.UnknownValueError:
            ptt3_tools.talk("No se pudo reconocer el audio")
            text = None
    return text






def play_on_youtube():  # Reproduce multimedia en Youtube
    ptt3_tools.talk("Claro, Indica el nombre de la canción o video")
    music = listen_and_transcribe()
    pywhatkit.playonyt(music)


def search_on_Wikipedia():  # Busca información en wikipedia, respuesta especifica = 5 orciones, resumida = 1
    ptt3_tools.talk("Claro, Indica el tema a buscar en wikipedia")
    issue = listen_and_transcribe()
    wikipedia.set_lang("es")
    ptt3_tools.talk("¿Desea una respuesta especifica o resumida?")
    if listen_and_transcribe()[:4] == "resu":
        word_length = 1
    else:
        word_length = 5
    ptt3_tools.talk("Buscando " + issue)

    try:
        informacion = wikipedia.summary(
            issue, sentences=word_length, auto_suggest=True, redirect=True
        )
        ptt3_tools.talk(informacion)
    except wikipedia.exceptions.PageError:
        ptt3_tools.talk("La página buscada no existe")
    except:
        ptt3_tools.talk(
            "Lo lamento, hubo un error no controlado al buscar la página, intentelo nuevamente"
        )


def tell_the_time():
    ptt3_tools.talk(
        " Son las "
        + str(current_time.hour)
        + " con "
        + str(current_time.minute)
        + " minutos "
    )


def indicate_the_date():
    ptt3_tools.talk(
        "Hoy es  "
        + str(current_time.day)
        + " del mes  "
        + str(current_time.month)
        + " del "
        + str(current_time.year)
    )


def buenDia():
    if current_time.hour >= 6 and current_time.hour < 13:
        ptt3_tools.talk("Buenos días Jeremy")
    elif current_time.hour >= 13 and current_time.hour < 18:
        ptt3_tools.talk("Buenas tardes Jeremy")
    else:
        ptt3_tools.talk("Buenas noches Jeremy")

    indicate_the_date()
    tell_the_time()


def buscarAccion(orden):
    if "reproduce" in orden:
        play_on_youtube()
    elif "hola" in orden or "buen dia" in orden or "buen día" in orden:
        buenDia()
    elif "fecha" in orden:
        indicate_the_date()
    elif "hora" in orden:
        tell_the_time()
    elif "busca" in orden:
        search_on_Wikipedia()
    elif "comandos" in orden:
        speak_Comands()
    else:
        ptt3_tools.talk("No se reconoció el comando")


def speak_Comands():
    ptt3_tools.talk("Los comandos disponibles son:")
    for x in comandos:
        ptt3_tools.talk(x + ", Función: " + comandos.get(x))





def iniciarAsistente():
    ptt3_tools.talk("Hola")
    resp = False
    while resp == False:
        #talk("Comandos disponibles") 
        print(end = "|\n")
        for i in comandos:
            print("'"+i+"'" + " : " + comandos.get(i),end="\n")
        print(end = "|\n")
        text = listen_and_transcribe()
        if text != None:
            #ptt3_tools.talk("Vuelve a intentarlo")
            resp = True
            # os.system("cls")#Limpia la consola en la terminal
    return text



comandofinal = iniciarAsistente().lower()
# 2.Se le indica la acción(lee)
# 3.Busca la acción
# 4. La ejecuta(Vuelve al estado inicial)
buscarAccion(comandofinal)

# 5.Pendiente de llamada(Paso 1)


# def lecturaOrden():
#    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
#        listener.adjust_for_ambient_noise(source)
#        voice = listener.listen(source)
#        engine.runAndWait()
#        try:
#            global orden
#            orden = listener.recognize_google(voice, language='es-PE')
#        except sr.UnknownValueError:
#            print("Google Speech Recognition could not understand audio")
#        except sr.RequestError as e:
#            print("Could not request results from Google Speech Recognition service;{0}".format(e))
#        ordenfinal = orden.lower()
#        return ordenfinal
