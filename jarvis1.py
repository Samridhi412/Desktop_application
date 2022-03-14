import sys
import time
from email import encoders
from email.mime.base import MIMEBase
import PyPDF2
import pyautogui
import pyjokes
import pyttsx3
import instaloader
import speech_recognition as sr
import datetime
import os
import cv2
import random
from twitterbot import *
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyPDF2
from pywhatkit.remotekit import start_server

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source,timeout=10,phrase_time_limit=2)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query
# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('sgarg7_be19@thapar.edu','sgarg@44')
#     server.sendmail('sgarg7_be19@thapar.edu',to,content)
#     server.close()

# to wish
def read_pdf():
    book=open("",'rb')
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages()
    speak(f"Total number of pages are: {pages}")
    speak("Enter the page number 0-indexed to be read")
    pg=int(input("Page Number:"))
    page=pdfreader.getPage(pg)
    text=page.extractText()
    speak(text)


def wish():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    print(hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning ,its {tt}")
    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon,its {tt}")
    else:
        speak(f"Good Evening,its {tt}")
    speak("I am jarvis maam please tell me how may I help you")
def news():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=2d4ebeda56b24ab8a0ff52191262a1f6"
    main_page=get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is:{head[i]}")

def start_prog():
    wish()
    while True:
        query=takecommand().lower()
        # logic building for tasks
        if "open notepad" in query:
            path1="C:\\WINDOWS\\notepad.exe"
            os.startfile(path1)
        elif "can you tweet" in query:
            speak("what should I tweet ma'am")
            query3="hello guys!!!!"
            tweet_now(query3)

    
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir=""
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")
        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=10)
            speak("According to wikipedia....")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')
        elif "open facebook" in query:
            webbrowser.open('www.facebook.com')
        elif "open stackoverflow" in query:
            webbrowser.open('www.stackoverflow.com')
        elif "open instagram" in query:
            webbrowser.open('www.instagram.com')
        elif "open linkedin" in query:
            webbrowser.open('www.linkedin.com')
        elif "open google" in query:
            speak("sir, what should I search on google")
            cm=takecommand().lower()
            webbrowser.open(f'{cm}')
        elif "send message" in query:
            speak("sir, what is the message")
            cm = takecommand().lower()
            hour = int(datetime.datetime.now().hour)
            min=int(datetime.datetime.now().minute)
            kit.sendwhatmsg("+917814479925",f"{cm}",13,16)
            time.sleep(120)
            speak("message has been sent")
        elif "song on youtube" in query:
            speak("which song would you like to listen maam")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")
        elif "email to sam" in query:

            speak("what should I say?")
            query=takecommand().lower()
            if "send a file" in query:
                email="sgarg7_be19@thapar.edu"
                password="garg3404"
                send_to_email="sgarg7_be19@thapar.edu"
                speak("okay ma'am, what is the subject for this email")
                query=takecommand().lower()
                subject=query
                speak("and ma'am what is the message for this email")
                query2=takecommand().lower()
                message=query2
                speak("please enter the correct path of the attachment into the shell")
                file_loc=input("please enter the path here: ")
                speak("please wait, I am sending email now")
                msg=MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['Subject']=subject
                msg.attach(MIMEText(message,'plain'))
                #setup attachment
                filename=os.path.basename(file_loc)
                attachment=open(file_loc,'rb')
                part=MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= %s"%filename)
                # attach attachment to MIMEMultipart object
                msg.attach(part)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email,password)
                text=msg.as_string
                server.sendmail(email,send_to_email, text)
                server.quit()
                speak("Email has been sent")
            else:
                email = "sgarg7_be19@thapar.edu"
                password = "garg3404"
                send_to_email = "sgarg7_be19@thapar.edu"
                message=query
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("Email has been sent")







        elif "you can sleep" in query:
            speak("Thanks for using me maam, have a wonderful day")
            sys.exit()
            # close any application
        elif "close notepad" in query:
            speak("ok maam, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        # set alarm
        elif "set alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir=''
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rundII23.exe powrprof.dII,SetSuspendState 0,1,0")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "hide all files" in query or "hide this folder" in query  or "visible for evryone" in query:
            speak("Plase tell me whether you want to hide the files or make them visible")
            query4=takecommand.lower()
            if "hide" in query4:
                os.system("attrib +h /s /d")
                speak("All files in the folder are now hidden")
            elif "visible" in query4:
                os.system("attrib -h /s /d")
                speak("All files in this folder are now visible for everyone. I hope all given commands are taken at piece")
            elif "leave it" in query4 or "leave for now" in query4:
                speak("OK...")        

        elif "tell me news":
            speak("Please wait Maam, fetching the latest news")
            news()
        elif "where i am" in query or "where we are" in query:
            speak("wait ma'am, let me check")
            try:
                ipadd=get('https://api.ipify.org').text
                print(ipadd)
                url='https://get.geojs.io/v1/ip/geo'+ipadd+'.json'
                geo_requests=get(url)
                geo_data=geo_requests.json()
                print(geo_data)
                city=geo_data['city']
                state=geo_data['state']
                country=geo_data['country']
                speak(f"Sir I am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry maam, Due to network issue i am not able to find where we are")
                pass    
        # check instagram profile
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Maam please enter the username correctly")
            name=input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Maam here is the profile of the user {name}")
            time.sleep(5)
            speak("would you like to download profile picture of this account")
            con=takecommand().lower()
            if "yes" in con:
                mod=instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("i am done maam profile picture is saved in your main folder, now i am ready for next command")
            else:
                pass   
        elif "read pdf" in query:
            read_pdf() 

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Please tell me the name of this screenshot file")
            name=takecommand().lower()
            speak("Please hold screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak( "i am done mam screenshot is saved in main folder now i am ready for next command")
        speak("Maam do you have any other work for me")
if __name__=="__main__":
    start_prog()








