import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

 opts = {
 "alias":('георгій', 'ігорьок', 'гарік', 'ігор'),
  "tbr":('скажи','розкажи','покажи', 'скільки','промов'),
  "cmds": {
        "ctime"('теперішній час','який зараз час','який час'),
        "radio"('включи музику','відтвори радіо','включи радіо'),
         "stupid1"('розкажи анікдот','розсміши мене','ти знаєш анікдоти')

    }    
 }
 
 def speak(what):
 	print(what)
 	speak_engine.say(what)
 	speak_engine.runAndWait()
 	speak_engine.shop()

 def callback(recognizer, audio):
 	try:
 		voice = recognizer.recognizer_google(audio, language = "ua-Ua").lover()
 		print("[log] Розпізнано: " + voice)

 		if voice.startswith(opts['alias']):
 			cmd = voice
 		for x in opts['alias']:
 			cmd =cmd.replace(x,"").strip()
 		for x in opts['tbr']:
 			cmd =cmd.replace(x,"").strip()
 			cmd = recognizer_cmd(cmd)
 			execute_cmd(cmd['cmd'])

 	except sr.UnknownValueError:
 	       print("[log] Голос не розпізнаний!")
 	except sr.UnknownValueError:
 	       print("[log] Невідома помилка, перевірте інтернет!")

def recognizer_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmd'].items():

        for x in v:
            vrt =fuzz.radio(cmd, x)
            if vrt > RC['cmd']:
                RC['cmd'] = c
                RC['parcent'] = vrt

    return RC
    
def execute_cmd(cmd):
   if cmd == 'ctime':
      now = datetime.datetime.now()               
    speak("Зараз" + str(now.hour) + ":" + str(now.minute))

   elif cmd == 'radio':
   	speak("Мій розробник не навчив мене анікдотам ... Ха ха ха")
  
   else:
   	print('Команда не розпізнана, повторіть!')

r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
	r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProoerty('voices')
speak_engine.setProperty('voice, voices[4].id')

speak("Мій розробник не навчив мене анікдотам ... Ха ха ха")

#speak("Добрий день, розробник")
#speak("Ігор слухає")

#stop_listening = r.listen_in_background(m, callback)
#while True: time.sleep(0.1) # infinity loop	

