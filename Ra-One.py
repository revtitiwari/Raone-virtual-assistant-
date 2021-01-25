import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
import playsound
import bs4
import gtts as gTTS
from pprint import pprint
from selenium import webdriver
import wolframalpha
from cryptography.hazmat.backends.openssl import ec
import webbrowser
from pygame import time
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back maam")
    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    speak("the current Time is")
    speak(Time)
    if hour>=6 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<24:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("RaaOne at your Service. Please tell me how can I help You? ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremil', 'yourpasssword')
    server.sendmail('senderemail', to, content)
    server.close()

def lighton():
    driver = webdriver.Chrome('C:\\Users\\Hp\\chromedriver_win32\\chromedriver.exe')
    driver.get("https://www.google.com/")
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()

def lightoff():
    driver = webdriver.Chrome('C:\\Users\Hp\\chromedriver_win32\\chromedriver.exe')
    driver.get("https://www.google.com/")
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()
            

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
         
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Anything else maa'm")     

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)
            speak("Anything else maa'm")     
        
        elif 'how is the weather' and 'weather' in query:

            url = 'https://www.accuweather.com/en/in/betul/189100/weather-forecast/189100'

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))
            speak("Anything else maa'm")     


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"maa'm, the time is {strTime}")
            speak("Anything else maa'm")     
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)
            speak("Anything else maa'm") 

        elif "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")
            speak('image is sucessfully captured')


        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)   


        elif 'email to ' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rvtiwari00245@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maa'm . I am not able to send this email")   

    def open_application(input): 
  
        if "chrome" in input: 
            speak("Google Chrome") 
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
            return
  
        elif "browser" in input: 
            speak("Opening browser") 
            os.startfile('"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"') 
            return
  
        elif "word" in input: 
            speak("Opening Microsoft Word") 
            os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.lnk"') 
            return
  
        elif "excel" in input: 
            speak("Opening Microsoft Excel") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016.lnk') 
            return 

        elif 'open code' in input:
            codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)
            return
        
        elif 'open youtube' in input:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            speak("Anything else maa'm") 

        elif 'open' in input:
            os.system('explorer C://{}'.format(query.replace('Open','')))
            speak("Anything else maa'm")

        else: 
            speak("Application not available") 
            return
        

    def search_web(query): 
  
        driver = webdriver.chrome() 
        driver.implicitly_wait(1) 
        driver.maximize_window() 
  
        if 'youtube' in query: 
  
            speak("Opening in youtube") 
            indx = query.split().index('youtube') 
            query = input.split()[indx + 1:] 
            driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
            return

        else: 
  
            if 'google' in query or 'search'in query: 
  
                indx = query.split().index('google') 
                query = input.split()[indx + 1:] 
                driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
            else: 
  
                driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
  
            return
  

    def about_you(query):
        if 'who are you' in query or 'what can you do' in query or 'about you' in query:
            speak('I am Ra-One version 1 point O an assistant I am made to help everyone and I love my job')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Revti tiwari on 3rd september 2020")
            print("I was built by Revti tiwari on 3rd september 2020")

        elif "How's you look like" in query:
            speak("Well! you can imagine me.I'm a handsome guy")

        else:
            speak("sorry! can't get your request" )

    def light_work():   
        
        if 'turn on lights' in query:
            speak("OK maa'm turning on the Lights")
            lighton()
            speak("Lights are on")   
        
        elif 'turn off lights' in query:
            speak("OK maa'm turning off the Lights")
            lightoff()
            speak("Lights are off")
            time.sleep(3)
            speak("Anything else maa'm")     

        elif "bye" in query or "stop" in query or "go offline" in query or "you can rest" in query:
            speak("Good bye maa'm,enjoy your day see you soon!")
            quit()

        elif "log off" in query or "sign out" in query or 'shutdown' in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
			
    

 
