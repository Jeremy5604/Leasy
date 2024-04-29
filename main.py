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

# Oculta la ventana de la terminal de windows
time.sleep(2)
ptg.hotkey("win", "d")


comandos = {
    "reproduce": " Reproduce un video en youtube",
    "hola": " saluda",
    "fecha": " Indica la fecha",
    "hora": " Indica la hora",
    "busca": " Investiga información en wikipedia",
    # "clase":" Inicia clases en meet según el horario",
    "Spotify": " Reproduce playlist de canciones favoritas",
    "modo Estudio": " Activa el modo de estudio rutinario",
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


# Carcateristicas del time


def SpotifyMusic():  # REVISIÓN DE ESTE MÉTODO
    os.system(
        "start C:\\Users\\Jerem\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
    )
    time.sleep(4)
    ptg.click(202, 426, 1)
    time.sleep(4)
    ptt3_tools.talk("Reproduciendo canciones favoritas en Spotify")
    ptg.click(530, 539, 1)


def abrirNavegador():  # REVISIÓN DE ESTE MÉTODO
    ptg.hotkey("win", "r")
    ptg.typewrite("opera.exe\n", 0.05)
    # mover hacia barra de navegacion y entrar a pagina de classroom
    time.sleep(2)
    ptg.moveTo(581, 62, 0.05)
    ptg.click()
    ptg.typewrite("https://classroom.google.com/u/1/\n", 0.04)
    time.sleep(4)  # time mientras carga pag

    def navegarClassroom():
        ptg.moveRel(0, 500, 0.05)
        ptg.click()

    def elegirClase(hora, min):
        haveError = False
        if time.strftime("%A") == "Monday":
            if (hora, min) >= (7, 00) and (hora, min) < (8, 30):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Ingenieria de Procesos")
                ptt3_tools.talk(
                    "El horario de la clase de Ingenieria de Procesos aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                ptt3_tools.talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651, 749, 0.05)  # Estadistica
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                ptt3_tools.talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057, 752, 0.05)  # Algebra Lineal
            elif (hora, min) >= (13, 00) and (hora, min) < (16, 00):
                ptt3_tools.talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041, 338, 0.05)  # Psicologia
            else:
                haveError = True
                ptt3_tools.talk(
                    "El día de hoy no tienes clases programadas para las "
                    + str(hora)
                    + " , "
                    + str(min)
                    + " horas"
                )
        elif time.strftime("%A") == "Tuesday":
            if (hora, min) >= (7, 00) and (hora, min) < (8, 30):
                ptt3_tools.talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236, 754, 0.05)  # Estructura de Datos
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                ptt3_tools.talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057, 752, 0.05)  # Algebra Lineal
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Ingenieria de Procesos")
                ptt3_tools.talk(
                    "El horario de la clase de Ingenieria de Procesos aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (14, 00) and (hora, min) < (16, 00):
                ptt3_tools.talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041, 338, 0.05)  # Psicologia
            else:
                haveError = True
                ptt3_tools.talk(
                    "El día de hoy no tienes clases programadas para las "
                    + str(hora)
                    + " , "
                    + str(min)
                    + " horas"
                )
        elif time.strftime("%A") == "Wednesday":
            if (hora, min) >= (7, 00) and (hora, min) < (8, 30):
                ptt3_tools.talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256, 350, 0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Ingenieria de Procesos")
                ptt3_tools.talk(
                    "El horario de la clase de Ingenieria de Procesos aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                ptt3_tools.talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236, 754, 0.05)  # Estructura de Datos
            elif (hora, min) >= (13, 00) and (hora, min) < (14, 00):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Química")
                ptt3_tools.talk(
                    "El horario de la clase de Química aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) >= (14, 00) and (hora, min) < (15, 00):
                ptt3_tools.talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041, 338, 0.05)  # Psicologia
            elif (hora, min) >= (15, 00) and (hora, min) < (16, 00):
                ptt3_tools.talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657, 347, 0.05)  # Microeconomia
            else:
                haveError = True
                ptt3_tools.talk(
                    "El día de hoy no tienes clases programadas para las "
                    + str(hora)
                    + " , "
                    + str(min)
                    + " horas"
                )
        elif time.strftime("%A") == "Thursday":
            if (hora, min) >= (7, 00) and (hora, min) < (8, 30):
                ptt3_tools.talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651, 749, 0.05)  # Estadistica
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                ptt3_tools.talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236, 754, 0.05)  # Estructura de Datos
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                ptt3_tools.talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256, 350, 0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (12, 00) and (hora, min) < (14, 00):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Química")
                ptt3_tools.talk(
                    "El horario de la clase de Química aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) >= (14, 00) and (hora, min) < (16, 00):
                ptt3_tools.talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657, 347, 0.05)  # Microeconomia
            else:
                haveError = True
                ptt3_tools.talk(
                    "El día de hoy no tienes clases programadas para las "
                    + str(hora)
                    + " , "
                    + str(min)
                    + " horas"
                )
        elif time.strftime("%A") == "Friday":
            if (hora, min) >= (7, 00) and (hora, min) < (8, 30):
                ptt3_tools.talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057, 752, 0.05)  # Algebra Lineal
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                ptt3_tools.talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256, 350, 0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                ptt3_tools.talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651, 749, 0.05)  # Estadistica
            elif (hora, min) >= (12, 00) and (hora, min) < (14, 00):
                haveError = True
                ptt3_tools.talk("Hoy tienes clase de Química")
                ptt3_tools.talk(
                    "El horario de la clase de Química aun no ha sido programada"
                )
                # ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) > (14, 00) and (hora, min) < (16, 00):
                ptt3_tools.talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657, 347, 0.05)  # Microeconomia
            else:
                haveError = True
                ptt3_tools.talk(
                    "El día de hoy no tienes clases programadas para las "
                    + str(hora)
                    + " , "
                    + str(min)
                    + " horas"
                )
        elif time.strftime("%A") == "Saturday":
            haveError = True
            ptt3_tools.talk("Hoy es sabado, no tienes clases para hoy")

        elif time.strftime("%A") == "Sunday":
            haveError = True
            ptt3_tools.talk("Hoy es sabado, no tienes clases para hoy")
        return haveError

    def navegacionMeet():
        ptg.click()
        time.sleep(2)
        ptg.moveTo(443, 651, 0.05)  # Boton meet
        ptg.click()
        time.sleep(5)
        ptg.moveTo(638, 778, 0.05)  # microfono
        ptg.click()
        time.sleep(1)
        ptg.moveTo(741, 781, 0.05)
        ptg.click()  # camara
        time.sleep(1)
        ptg.moveTo(1355, 587, 0.5)

    def mensajeFinal():
        ptt3_tools.talk("Ya puedes iniciar la clase, solo falta la confirmación")

    # abrirNavegador()
    # navegarClassroom()

    if not (elegirClase(time.hour, time.minute)):
        navegacionMeet()
        mensajeFinal()
    else:
        ptt3_tools.talk("Proceso Terminado")


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
    # elif 'clase' in orden:
    # ptt3_tools.talk("Entendido.")
    # ptt3_tools.talk("Abriendo classroom")
    #
    elif "spotify" in orden:
        SpotifyMusic()
    elif "estudio" in orden:
        modoEstudio()
    elif "comandos" in orden:
        speak_Comands()
    else:
        ptt3_tools.talk("No se reconoció el comando")


def speak_Comands():
    ptt3_tools.talk("Los comandos disponibles son:")
    for x in comandos:
        ptt3_tools.talk(x + ", Función: " + comandos.get(x))


def search_on_navegator(ruta):
    ptg.click(425, 67)
    ptg.hotkey(ruta + "\n")
    pass


def iniciarAsistente():
    ptt3_tools.talk("Hola")
    resp = False
    while resp == False:
        # ptt3_tools.talk("Comandos disponibles")
        ##print(end = "|")
        # for i in comandos:
        # print(i,end="| |")
        # print(end = "|\n")
        text = listen_and_transcribe()
        if text != None:
            # ptt3_tools.talk("Vuelve a intentarlo")
            resp = True
            # os.system("cls")#Limpia la consola en la terminal
    return text


def modoEstudio():
    ptt3_tools.talk("Iniciando modo Estudio")
    # os.system("start C:\\Users\\Jerem\\AppData\\Local\\Programs\\Notion\\Notion.exe")
    ptt3_tools.talk("Retomando curso en Cisc for All")
    # C:\Users\Jerem\AppData\Local\Programs\Opera GX
    os.system(
        "start C:\\Users\\Jerem\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
    )
    ptt3_tools.talk("Retomando guía de programación en Java")
    search_on_navegator(
        "https://skillsforall.com/launch?id=064f3246-8ddc-4375-8e9c-5e3594ca7744"
    )
    pass


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
