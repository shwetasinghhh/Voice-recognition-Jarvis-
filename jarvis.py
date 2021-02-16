import pyttsx3 #external library installed using command "pip install pyttsx3"---->FOR TEXT TO SPEECH CONVERSION
import datetime  #BUILT-IN LIBRARY--->FOR KNOWING CURRENT DATE-TIME
import speech_recognition as sr  #EXTERNAL LIBRARY INSTALLED USING pip install SpeechRecognition---->FOR SPEECH TO TEXT CONVERSION
import  wikipedia  #EXTERNAL LIBRARY INSTALLED USING pip install wikipedia---->FOR SEARCHING ON WIKIPEDIA
import smtplib  #BUILT-IN FUNCTION--->FOR SENDING EMAILS
import pyautogui  #EXTERNAL LIBRARY pip install pyautogui---> FOR SCREENSHOT
import webbrowser as wb  #BUILT-IN FUNCTION--->FOR CHROME SEARCH
import os     #built-in library --->FOR SHUTDOWN,LOGOUT,RESTARTING THE SYSTEM
import psutil #EXTERNAL LIBRARY --->for CPU AND BATTERY USAGE
import pyjokes #EXTERNAL LIBRARY-->FOR JOKES

engine=pyttsx3.init() 

#USER DEFINED FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#KNOW THE CURRENT TIME
def current_time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

speak("mera naam shweta")
current_time()

#KNOW TODAY'S DATE WITH YEAR AND MONTH
def date_today():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)
date_today()

#GREETINGS FUNCTION
def wishme():
    speak("welcome back sir")
    speak("the current time is")
    current_time()
    speak("the current date is")
    date_today()

#RETURNS HOUR BY WHICH WE DECIDE USING IF ELSE STATEMENT OF THE TIME OF DAY
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("Alexa at your service please tell me how can i help you")
wishme()

#SPEECH TO TEXT CONVERSION
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
       
    except Exception as e:
       # print(e)
        speak("Please repeat")  
        return "None"
    return query

takeCommand()

#SEND EMAIL FUNCTION
def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.echo()
    server.starttls()
    server.login('shefalikumari780@gmail.com','Swinkykumari@1999')
    server.sendmail('shefalikumari780@gmail.com',to,content)
    server.close()

#SCREENSHOT FUNCTION
def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\\Desktop\\work\\jarvis\\ss.png")

#CPU  AND BATTERY UPDATE FUNCTION
def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at" +usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

#JOKES FUNCTION
def jokes():
    speak(pyjokes.get_joke())


#MAIN FUNCTION TO PERFORM TASKS
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        #TIME FUNCTION CALLING
        if 'time' in query:
            current_time()

        #DATE FUNCTION CALLING
        elif 'date' in query:
            date_today()

        #WIKIPEDIA SEARCH FUNCTION CALLING
        elif 'wikipedia' in query:
            speak("searching") 
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        #SEND EMAIL FUNCTION CALLING
        elif 'send email' in query:
            try:
                speak("what do yo want to say")
                content=takeCommand()
                send_email('oraonjohnniraj68@gmail.com',content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send mail")
        
        #CHROME SEARCH CALLING
        elif 'search in chrome' in query:
            speak("what should i search")
            chromepath('C:/Program Files(x86)/Google/Chrome/Application/Chrome.exe %s')
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        #LOGOUT,SHUTDOWN AND RESTART FUNCTION CALLING
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        #PLAY SONGS
        elif 'play songs' in query:
            songs_dir='D:\\Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        #REMEMBER FUNCTION CALLING
        elif 'remember that' in query:
            speak("what should I remember")
            data=takeCommand()
            speak("you said me to remember"+data)
            remember=open('remember.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('remember.txt','r')
            speak("you said me to remember that"+remember.read())

        #SCREENSHOT CALLING
        elif 'screenshot' in query:
            screenshot()
            speak("screenshot successfully taken")

        #CPU AND BATTERY USAGE CALLING
        elif 'cpu' in query:
            cpu() 

        #JOKES CALLING 
        elif 'jokes' in query:
            jokes()
        
        #EXIT THE LOOP
        elif 'offline' in query:
            quit()
     