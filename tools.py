import pyautogui 
import speech_recognition 
import pyttsx3


engine = pyttsx3.init()



class pyautogui_tools:

    def __init__(self) -> None:
        pass

    def locate_pointer(self):
        pyautogui.mouseInfo()

      

class speech_recognition_tools:
    def __init__(self):
        pass

    def create_recognizer(self):
        return speech_recognition.Recognizer()

    
    
    
class pyttsx3_tools: 
    def __init__(self) -> None:
        pass
    
    def init_pyttsx3(self):
        
        return pyttsx3.init()
        
    def talk(self,texto):#Reproduce texto en altavoz
        engine.say(texto)
        engine.runAndWait()
        pass

    def set_Properties_voice(rate = 153,volume = 1.0, num_voice = 0,lang = "es"):
        engine.setProperty('rate',rate)
        engine.setProperty('volume',volume)
        voices = engine.getProperty('voices')  #Obtener la lista de voces disponibles en tu sistema
        engine.setProperty('voice', voices[num_voice].id)  # Seleccionar una voz específica (por defecto, la primera de la lista)
        engine.setProperty('lang', lang)

    
    def test_voice(self,engine):
        engine.say("Esta es una prueba de voz con pyttsx3")
        engine.runAndWait()
        pass
        

        
