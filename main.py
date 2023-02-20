import pyttsx3, speech_recognition as sr
import AI

BotVoice = pyttsx3.init()
def speak(txt):
    BotVoice.setProperty('rate', 175)
    BotVoice.say(txt)
    BotVoice.runAndWait()


# verbal input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") # in output window
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognising...") # in output window
        query = r.recognize_google(audio, language="en-in")
        print(ask) # in input window
        return query
    except:
        return "__Err__"


botName = "Charon"
print(f"Hello I am {botName}, I am here to answer all your queries and help you with your work") # in output window
speak(f"Hello I am {botName}, I am here to answer all your queries and help you with your work")
while True:
    ask = listen()
    if ask == "__Err__":
        print("Sorry there was some error in catching your voice. Please try speaking again.") # in output window
        speak("Sorry there was some error in catching your voice. Please try speaking again.")
    elif "exit" in ask.lower():
        exit()
    else:
        txt = AI.out(ask)
        print(txt) #in output window
        speak(txt)


    
