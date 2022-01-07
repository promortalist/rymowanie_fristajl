#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import pickle
import speech_recognition as sr
open_file = open("sjp.pkl", "rb")
lista = pickle.load(open_file)
open_file.close()
def redukcja(x):
  return list(dict.fromkeys(x))

def rhyme(word):
    wynik = []
    if len(word) >= 7:
       for x in lista:
           if word[-5:] in x[-5:]:
              wynik.append(x)
    elif len(word) <=6:
       for x in lista:
           if word[-4:] in x[-4:]:
              wynik.append(x)
    final = redukcja(wynik)
    print("Dostępne rymy do "+word+": "+str(final))


# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
         print("Rapuj ziomuś!")
         audio = r.listen(source)
# Speech recognition using Google Speech Recognition
         try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
             # print("Powiedziałeś: " + r.recognize_google(audio,language="pl-PL"))
             word = r.recognize_google(audio,language="pl-PL")
             rhyme(word)
    #        print("You said: " + r.recognize_google(audio))
         except sr.UnknownValueError:
             print("Google Speech Recognition nie kmini tego co nawijasz")
         except sr.RequestError as e:
             print("Could not request results from Google Speech Recognition service; {0}".format(e))
