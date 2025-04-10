from tkinter import *
import time
from PIL import Image,ImageTk
from tkinter import ttk
import pyttsx3
import threading



check = False




def CurrentTime():
    displayTime = time.strftime("%H:%M:%S: %p")
    
    newLabel.config(text=f"{displayTime}")
    setAlarm(displayTime)
    newLabel.after(200,CurrentTime)

def check_button():
    global check 
    check = True

def speak(word):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   
    for i in range(3):
     engine.say(word)
     engine.runAndWait()

def setAlarm(time):
      if check:  
        H = hour_Combo.get()
        M = minute_Combo.get()
        A_or_P = AM_combo.get()
        give_time = f"{H}:{M}:00: {A_or_P}"
        print(give_time,time)
        i = 0
        if give_time == time and i == 0:
            i += 1
            threading.Thread(target=speak,args=("wake up",)).start()



window = Tk()

window.title("Digital Clock")

window.geometry("800x600")
window.resizable(False,False)

bgImage = Image.open("clock.png")
bgImage = bgImage.resize((800,500))
bgPhoto = ImageTk.PhotoImage(bgImage)

BgLabel = Label(window,image=bgPhoto)
BgLabel.place(x=0,y=0,relheight=1,relwidth=1)

newLabel = Label(window,text="",font=("arial",50),fg="sky blue",bg="black")
newLabel.place(x=160,y=230)

Hour_choice = ['00','01','02', '03', '04', '05', '06', '07', '08', '09', 10, 
 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
 21, 22, 23]
minute_choice = minute_choices = [
    '00','01','02', '03', '04', '05', '06', '07', '08', '09', 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60
]
AM_choice = ['AM','PM']
hour_Combo = ttk.Combobox(window,values = Hour_choice)
hour_Combo.set('Hour')
hour_Combo.place(x=20,y=560,width=60)

minute_Combo = ttk.Combobox(window,values = minute_choice)
minute_Combo.set("Min")
minute_Combo.place(x=80,y=560,width=60)

AM_combo = ttk.Combobox(window,values=AM_choice)
AM_combo.set('AM/PM')
AM_combo.place(x=140,y=560,width=80)

Alarm_Button = Button(window,text="Set Alarm",font=("arial",10),command=check_button)
Alarm_Button.place(x=650,y=560,width=100)

CurrentTime()

window.mainloop()