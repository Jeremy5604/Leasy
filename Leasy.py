import pyautogui as ptg
ptg.hotkey("win","d")#Oculta la ventana de la terminal de windows
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import time
from datetime import datetime



import pyautogui as ptg
#Para estudio 
import os
import sys
import platform


#ptg.mouseInfo()

#Variables principales


receptor = sr.Recognizer()
tiempoSincronizado = datetime.now()




#características de voz 
engine = pyttsx3.init()
engine.setProperty('rate', 150)
comandos = {"reproduce":" Reproduce un video en youtube",
            "hola":" saluda",
            "fecha":" Indica la fecha",
            "hora":" Indica la hora",
            "busca":" Investiga información en wikipedia",
            "clase":" Inicia clases en meet según el horario",
            "Spotify":" Reproduce playlist de canciones favoritas",
            "modo Estudio":" Activa el modo de estudio rutinario",
            "comandos": " Informa al usuario sobre los comandos disponibles"}


#Métodos principales

def listen_and_transcribe():#Recibe texto oralmente
    with sr.Microphone() as source:
        talk('Escuchando...')
        #audio = receptor.adjust_for_ambient_noise(source,duration=5)
        audio = receptor.listen(source)
        try:
            text = receptor.recognize_google(audio, language='es-ES')
        except sr.UnknownValueError:
            talk('No se pudo reconocer el audio')
            text = None
    return text

def talk(texto):#Reproduce texto en altavoz
    engine.say(texto)
    engine.runAndWait()
    pass










# Carcateristicas del time







def SpotifyMusic():#REVISIÓN DE ESTE MÉTODO
    os.system("start C:\\Users\\Jerem\\AppData\\Roaming\\Spotify\\Spotify.exe ")
    time.sleep(4)
    ptg.click(214,315,1)
    time.sleep(2)
    talk("Reproduciendo canciones favoritas en Spotify")
    ptg.click(552,493,1)


def abrirNavegador():#REVISIÓN DE ESTE MÉTODO
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
            if (hora, min) >= (7,00) and (hora, min) < (8, 30):
                haveError=True
                talk("Hoy tienes clase de Ingenieria de Procesos")
                talk("El horario de la clase de Ingenieria de Procesos aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651,749,0.05)  # Estadistica
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057,752,0.05)  # Algebra Lineal
            elif (hora, min) >= (13, 00)and (hora, min) < (16, 00):
                talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041,338,0.05)  # Psicologia
            else:
                haveError=True
                talk(
                    "El día de hoy no tienes clases programadas para las " + str(hora) + " , " + str(min)+" horas"
                )
        elif time.strftime("%A") == "Tuesday":
            if (hora, min) >= (7,00) and (hora, min) < (8, 30):
                talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236,754,0.05)  # Estructura de Datos
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057,752,0.05)  # Algebra Lineal
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                haveError=True
                talk("Hoy tienes clase de Ingenieria de Procesos")
                talk("El horario de la clase de Ingenieria de Procesos aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (14, 00)and (hora, min) < (16, 00):
                talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041,338,0.05)  # Psicologia
            else:
                haveError=True
                talk(
                    "El día de hoy no tienes clases programadas para las " + str(hora) + " , " + str(min)+" horas"
                )
        elif time.strftime("%A") == "Wednesday":
            if (hora, min) >= (7,00) and (hora, min) < (8, 30):
                talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256,350,0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                haveError=True
                talk("Hoy tienes clase de Ingenieria de Procesos")
                talk("El horario de la clase de Ingenieria de Procesos aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Ingenieria de Procesos
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236,754,0.05)  # Estructura de Datos
            elif (hora, min) >= (13, 00) and (hora, min) < ( 14, 00):
                haveError=True
                talk("Hoy tienes clase de Química")
                talk("El horario de la clase de Química aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) >= (14, 00)and (hora, min) < (15, 00):
                talk("Hoy tienes clase de Psicología")
                ptg.moveTo(1041,338,0.05)  # Psicologia
            elif (hora, min) >= (15, 00)and (hora, min) < (16, 00):
                talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657,347,0.05)  # Microeconomia
            else:
                haveError=True
                talk(
                    "El día de hoy no tienes clases programadas para las " + str(hora) + " , " + str(min)+" horas"
                )
        elif time.strftime("%A") == "Thursday":
            if (hora, min) >= (7,00) and (hora, min) < (8, 30):
                talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651,749,0.05)  # Estadistica
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                talk("Hoy tienes clase de Estructura de Datos")
                ptg.moveTo(236,754,0.05)  # Estructura de Datos
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256,350,0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (12, 00) and (hora, min) < ( 14, 00):
                haveError=True
                talk("Hoy tienes clase de Química")
                talk("El horario de la clase de Química aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) >= (14, 00)and (hora, min) < (16, 00):
                talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657,347,0.05)  # Microeconomia
            else:
                haveError=True
                talk(
                    "El día de hoy no tienes clases programadas para las " + str(hora) + " , " + str(min)+" horas"
                )
        elif time.strftime("%A") == "Friday":
            if (hora, min) >= (7,00) and (hora, min) < (8, 30):
                talk("Hoy tienes clase de Algebra Lineal")
                ptg.moveTo(1057,752,0.05)  # Algebra Lineal
            elif (hora, min) >= (8, 30) and (hora, min) < (10, 00):
                talk("Hoy tienes clase de Concepción Física del Universo")
                ptg.moveTo(256,350,0.05)  # Concepción Fisica Del Universo
            elif (hora, min) >= (10, 00) and (hora, min) < (12, 00):
                talk("Hoy tienes clase de Estadistica")
                ptg.moveTo(651,749,0.05)  # Estadistica
            elif (hora, min) >= (12, 00) and (hora, min) < (14, 00):
                haveError=True
                talk("Hoy tienes clase de Química")
                talk("El horario de la clase de Química aun no ha sido programada")
                #ptg.moveTo(657,347,0.05)  # Quimica
            elif (hora, min) > (14, 00) and (hora, min) < (16, 00):
                talk("Hoy tienes clase de Microeconomia")
                ptg.moveTo(657,347,0.05)  # Microeconomia
            else:
                haveError=True
                talk(
                    "El día de hoy no tienes clases programadas para las " + str(hora) + " , " + str(min)+" horas"
                )
        elif time.strftime("%A") == "Saturday":
            haveError=True
            talk("Hoy es sabado, no tienes clases para hoy")

        elif time.strftime('%A') == 'Sunday':
            haveError=True
            talk("Hoy es sabado, no tienes clases para hoy")
        return haveError

    def navegacionMeet():
        ptg.click()
        time.sleep(2)
        ptg.moveTo(443,651,0.05)#Boton meet
        ptg.click()
        time.sleep(5)
        ptg.moveTo(638,778,0.05)#microfono
        ptg.click()
        time.sleep(1)
        ptg.moveTo(741,781,0.05)
        ptg.click()#camara
        time.sleep(1)
        ptg.moveTo(1355,587, 0.5)

    def mensajeFinal():
        talk("Ya puedes iniciar la clase, solo falta la confirmación")



    #abrirNavegador()
    #navegarClassroom()

    if not (elegirClase(time.hour,time.minute)):
        navegacionMeet()
        mensajeFinal()
    else:
        talk("Proceso Terminado")

def play_on_youtube():#Reproduce multimedia en Youtube
    talk("Claro, Indica el nombre de la canción o video")
    music = listen_and_transcribe()
    pywhatkit.playonyt(music)

def search_on_Wikipedia():#Busca información en wikipedia, respuesta especifica = 5 orciones, resumida = 1
    talk("Claro, Indica el tema a buscar en wikipedia")
    issue = listen_and_transcribe()
    wikipedia.set_lang('es')
    talk("¿Desea una respuesta especifica o resumida?")
    if listen_and_transcribe()[:4] == "resu":
        word_length = 1
    else:
        word_length = 5
    talk('Buscando ' + issue)
    informacion = wikipedia.summary(issue, sentences = word_length, auto_suggest = True,redirect=True)
    talk(informacion)
    
def tell_the_time():
    talk(" Son las " + str(tiempoSincronizado.hour) + " con " + str(tiempoSincronizado.minute) + " minutos ")

def indicate_the_date():
    talk("Hoy es  " + str(tiempoSincronizado.day) + " del mes  " + str(tiempoSincronizado.month) + " del " + str(tiempoSincronizado.year))
    
def buenDia():
    if tiempoSincronizado.hour >= 6 and tiempoSincronizado.hour < 13:
        talk("Buenos días Jeremy")
    elif tiempoSincronizado.hour >= 13 and tiempoSincronizado.hour < 18:
        talk("Buenas tardes Jeremy")
    else:
        talk("Buenas noches Jeremy")

    indicate_the_date()
    tell_the_time()

def buscarAccion(orden):
    if 'reproduce' in orden:
        play_on_youtube()
    elif 'hola' in orden or 'buen dia' in orden or 'buen día' in orden:
        buenDia()
    elif 'fecha' in orden:
        indicate_the_date()
    elif 'hora' in orden:
        tell_the_time()
    elif 'busca' in orden:
        search_on_Wikipedia()
    #elif 'clase' in orden:
        #talk("Entendido.")
        #talk("Abriendo classroom")
        #iniciarClase()
    elif 'spotify' in orden:
        SpotifyMusic()
    elif 'estudio' in orden:
        modoEstudio()
    elif 'comandos' in orden:
        speak_Comands()
    else:
        talk('No se reconoció el comando')



def speak_Comands():
     talk("Los comandos disponibles son:")
     for x in comandos:
         talk(x + ", Función: " + comandos.get(x))


def search_on_navegator(ruta):
    ptg.click(425,67)
    ptg.hotkey(ruta + "\n")
    pass




def iniciarAsistente():
    talk("Hola")
    resp = False
    while (resp == False):
        #talk("Comandos disponibles") 
        ##print(end = "|")
        #for i in comandos:
            #print(i,end="| |")
        #print(end = "|\n")
        text = listen_and_transcribe()
        if text!= None:
            #talk("Vuelve a intentarlo")
            resp= True
            #os.system("cls")#Limpia la consola en la terminal
    return text





def modoEstudio():
    talk("Iniciando modo Estudio")
    os.system("start C:\\Users\\Jerem\\AppData\\Local\\Programs\\Notion\\Notion.exe")
    talk("Retomando curso en Cisc for All")
    os.system("start C:\\Users\\Jerem\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
    talk("Retomando guía de programación en Java")
    search_on_navegator("https://skillsforall.com/launch?id=064f3246-8ddc-4375-8e9c-5e3594ca7744")
    pass


















comandofinal = iniciarAsistente().lower()
# 2.Se le indica la acción(lee)
# 3.Busca la acción
# 4. La ejecuta(Vuelve al estado inicial)
buscarAccion(comandofinal)

    # 5.Pendiente de llamada(Paso 1)







#def lecturaOrden():
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


