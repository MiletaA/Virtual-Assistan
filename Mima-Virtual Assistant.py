import speech_recognition as sr # Prepoznaje govor
import playsound # Pušta audio
from gtts import gTTS # google text to speech
import random
from time import ctime # Vreme
import webbrowser # Otvaranje Pretraživač
import ssl
import time
import os # Briše audio fajl
import subprocess
import sys
import urllib.request


class person:
    name = ''
    def setName(self, name):
        self.name = name
class MiMa:
    name = ''
    def setName(self, name):
        self.name = name

def glasovna_komanda (terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # Zvuk u text
def record_audio(ask=False):
    with sr.Microphone() as source: # Mikrofon kao izvor
          if ask:
            speak(ask)
    audio = ''
    with sr.Microphone() as source:
        
        audio = r.listen(source, phrase_time_limit=5)
    print("Stop.")
    try:
        text = r.recognize_google(audio,language='sr')
        print("Ti : ", text)
        return text
    except:
        speak("Ne mogu da razumem vaš zvuk, pokušajte ponovo!")
        return 0


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='sr') # text to speech(Glas)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # Čuva kao mp3
    playsound.playsound(audio_file) # Pušta audio fajl
    print(f"MiMa: {audio_string}") # printa mimine reči
    os.remove(audio_file) # briše audio

def respond(voice_data):
    #1: pozdrav    
    if glasovna_komanda (["pozdrav","zdravo"]):
        greetings = [f"zdravo,kako vam mogu pomoći {person_obj.name}", f"hey, what's up? {person_obj.name}", f"slušam {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    #2: ime
    if glasovna_komanda (["ko si ti","kako se zoveš","koje je tvoje ime"]):
            speak( '''Zdravo,ja sam Mima,Vaš lični asistent.
            Ovde sam da vam olakšam život.
            Možete mi narediti da obavljam razne zadatke kao što su otvaranje aplikacija, pretraživanje na Internetu,
            prikazivanje vremenske prognoze i tako dalje''')
       
    if glasovna_komanda (["moje ime je"]):
        person_name = voice_data.split("je")[-1].strip()
        speak(f"okaj, zapamtiću vaše ime {person_name}")
        person_obj.setName(person_name) #zapamti ime u  person object

    #3: Pozdrav 2
    if glasovna_komanda (["kako si"]):
        speak(f"super sam,hvala na pitanju {person_obj.name}")

    #4: vreme
    if glasovna_komanda (["Koliko je sati","Koliko ima časova"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours  + "i" + minutes 

        speak(time)

    #5: Pretraži google (Pretraži + željeni termin)
    if glasovna_komanda (["pretraži"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("pretraži")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'ovo sam pronašla u vezi  {search_term} na google')

    #6: pretraži youtube (Željeni termin + Youtube/jutjub/)
    if glasovna_komanda (["YouTube" , "na youtube-u"]):
        search_term = voice_data.split("YouTube")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'ovo sam pronašla u vezi {search_term} na youtube')
   
    #7: Vremenska prognoza za + grad/mesto
    if glasovna_komanda (["vremenska prognoza"]):
        search_term = voice_data
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak("Pronašla sam vremensku prognozu na googlu")
    #8: otvaranje notepada
    if glasovna_komanda (["Zapiši", "napiši", "sveska"]):
     subprocess.call(['notepad.exe'])

    
    #9: Otvaranje Gmail-a 
    if glasovna_komanda (["otvori mail","Gmail","otvori mejlove"]):
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        speak("Ovde možete da proverite Vaše mejlove")
  
    #10 papir kamen makaze
    if glasovna_komanda (["igra"]):
        voice_data = record_audio("izaberite izmedju kamena,papira i makaza")
        moves=["kamen", "papir", "makaze"]
        cmove=random.choice(moves)
        pmove=voice_data
        

        speak("Ja sam izabrala " + cmove)
        speak("Vi ste izabrali " + pmove)
       
        if pmove==cmove:
            speak("niko nije pobedio")
        elif pmove== "kamen" and cmove== "makaze":
            speak("vi ste pobedili")
        elif pmove== "kamen" and cmove== "papir":
            speak("Ja sam pobedila")
        elif pmove== "papir" and cmove== "kamen":
            speak("Vi ste pobedili")
        elif pmove== "papir" and cmove== "makaze":
            speak("Ja sam pobedila")
        elif pmove== "makaze" and cmove== "papir":
            speak("Vi ste pobedili")
        elif pmove== "makaze" and cmove== "kamen":
            speak("Ja sam pobedila")

    
    #11 Gašenje
    if glasovna_komanda (["ugasi se", "doviđenja", "gasi se"]):
        speak("okej,doviđenja")
        exit() 

time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio("slušam vas") # Glasovna komanda
    respond(voice_data) # odgovor


