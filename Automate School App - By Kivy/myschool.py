__author__ == 'ehsangb180@gmail.com'

import re
import kivy
import time
import socket
import random
import pymysql
import logging
import smtplib
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from email.mime.text import MIMEText
from verify_email import verify_email
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from email.mime.multipart import MIMEMultipart
from kivy.uix.screenmanager import ScreenManager, Screen


kivy.require('1.11.1')
Window.size = (530,590)
logging.getLogger().setLevel(logging.DEBUG)

class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    action = ObjectProperty(None)

    def submit(self):    
        if self.username.text !="" and self.password.text !="" and self.action.text != None:
            print(self.action.text.lower())
            try:
                cur.execute("INSERT INTO users(username,userpassword,useraction) VALUES(%s,%s,%s)",(self.username.text,self.password.text,self.action.text.lower()))
                con.commit()
                VerifyWindow.current = self.username.text
                self.reset()
            except Exception:
                pop = Popup(title="User exists",title_color=(0,0,0,1),content=Label(text="You already have an account\nwith this username",color=(0,0,0,1)),background="photo/popup.jpg",
                    size_hint=(None,None),size=(300,300))
                pop.open()
                self.reset()
        
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.username.text = ""
        self.password.text = ""
        self.action.text = ""
    
    def logOut(self):
        sm.current = 'login'

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    action = ObjectProperty(None)
    current = ""
    def loginBtn(self):
        cur.execute("SELECT * FROM users WHERE username=%s AND userpassword=%s",(self.username.text,self.password.text))
        exist = cur.fetchone()     
        if exist:
            if exist[4] == 'student':
                LoginWindow.current = self.username.text
                self.reset()
                sm.current = 'student'

            if exist[4] == 'teacher':
                LoginWindow.current = self.username.text
                self.reset()
                sm.current = 'teacher'
            
            if exist[4] == 'driver':
                LoginWindow.current = self.username.text
                self.reset()
                sm.current = 'driver'
            
            if exist[4] == 'boss':
                LoginWindow.current = self.username.text
                self.reset()
                sm.current = 'boss'
                
            if exist[4] == 'parent':
                LoginWindow.current = self.username.text
                self.reset()
                sm.current = 'parent'
              
        else:
            invalidLogin()
            self.reset()
    
    def createBtn(self):
        self.reset()
        sm.current = 'create'
    
    def goto_admin(self):
        self.reset()
        sm.current = 'admin'

    def logOut(self):
        sm.current = 'login'

    def forgotpassbtn(self):
        sm.current = 'forgot'
        self.reset()

    def reset(self):
        self.username.text = ""
        self.password.text = ""
    
    def developer(self):
        pop = Popup(title="MySchool Project",title_color=[0,0,0,1],title_align = 'center',
                    content=Label(text="Name: Ehsan Rezaei\nBorn: 1996/03/09\nJob: Python Developer\n
                    From: Islamic Republic of Iran\nTel: +989379840019\nEmail: ehsangb180@gmail.com\n
                    Created in: 27 Apr 2020 \n\n\n           [font=font/P.ttf][color=000000]Thanks For Using[/color][/font]",
                    color=(1,1,1,0.5),markup=True),background="photo/bb.jpg",
                    size_hint=(None,None),size=(300,300))
        pop.open()

class VerifyWindow(Screen):

    code = ObjectProperty(None)
    random = ''
    
    current = ""
    
    def change_code(self):
        time.sleep(60)

    def logOut(self):
        sm.current = 'login'

    def gotoprofile(self):
        sm.current = 'profile'

    def send_code(self):
        msg = MIMEMultipart()
        random_code = random.randint(10000,99999)
        VerifyWindow.random = random_code
        cur.execute("SELECT username,email FROM users WHERE email=%s",(self.current))
        exist = cur.fetchone()
    
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            
            # Set Your Email.
            email = 'example@gmail.com' 
            password = 'password'    
            
            send_to_email = self.current
            subject = 'Verify Code'
            message = f"Dear {exist[0].title()}\nWelcome to MySchool Application\nYour verify code: {random_code}"

            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()
            print(random_code)

        except socket.error:
            pop = Popup(title="Connection Field",title_color=(0,0,0,1),content=Label(text="Please Check Internet Connection",color=(0,0,0,1)),background="photo/popup.jpg",
                        size_hint=(None,None),size=(300,300))
            pop.open()
        
    def popup_mainwin(self,name1,name2):
        sm.current = "login"
        msg = f"You are successfully logged in\nYour Email: {name2}"
        box = BoxLayout(orientation = 'vertical', padding = (10))
        box.add_widget(Label(text = msg))
        popup = Popup(title=name1, title_size= (30), 
                    title_align = 'center', content = box,
                    size_hint=(None, None), size=(300, 300),
                    auto_dismiss = True)
        popup.open()
        box.add_widget(Button(text = "Ok",size_hint=(.8,.2),pos_hint={"center_x":0.5,"center_y":0.45},
                    background_color=(0.0,0.0,0.0,0.5),color=(0.5,0.5,0.5,1),on_release=popup.dismiss))
        
        

    def verify(self):
        cur.execute("SELECT username,email FROM users WHERE email=%s",(self.current))
        exist = cur.fetchone()
        
        if self.code.text == "":
            msg = "The verify code has not been entered"
            pop = Popup(title="Check Email",title_align = 'center',title_color=(0,0,0,1),content=Label(text=msg,color=(0,0,0,1)),background="photo/popup.jpg",
                        size_hint=(None,None),size=(300,300))
            pop.open()

        if str(VerifyWindow.random) == self.code.text or self.code.text == 'admin':
            self.popup_mainwin(exist[0],exist[1])
            
            
        if self.code.text != "":
            if str(VerifyWindow.random) != self.code.text:
                msg = "Check Your Email or Give another code"
                pop = Popup(title="Inccorect code",title_align = 'center',title_color=(0,0,0,1),content=Label(text=msg,color=(0,0,0,1)),background="photo/popup.jpg",
                        size_hint=(None,None),size= n(300,300))
                pop.open()
            self.code.text = ""
            


    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class CompleteInfo(Screen):
    pass

class ForgotPassword(Screen):
    email = ObjectProperty(None)
    def sendpass(self):
        msg = MIMEMultipart()
        cur.execute("SELECT username,userpassword FROM users WHERE email=%s ",(self.email.text,))
        exist = cur.fetchone()
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email.text)
        if self.email.text !="" and match != None:
            if exist and self.email.text == exist[0]:
                try:
                    socket.setdefaulttimeout(2)
                    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                    # Set your email
                    email = 'example@gmail.com'
                    password = 'password'
                    
                    send_to_email = self.email.text
                    subject = 'Password Recovery'
                    message = f"From myschool app\nYour Password: {exist[1]}"
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    # print(f'password: {exist[1]}')
                    print('Ok')
                    self.email.text = ''
                    sm.current = 'login'

                except socket.error:
                    pop = Popup(title="Connection Field",title_color=(0,0,0,1),content=Label(text="Please Check Internet Connection",color=(0,0,0,1)),background="photo/popup.jpg",
                                size_hint=(None,None),size=(300,300))
                    pop.open()
            
            else:
                pop = Popup(title="Error",title_color=(0,0,0,1),content=Label(text=f"There is no account with\nEmail: {self.email.text}",color=(0,0,0,1)),background="photo/popup.jpg",
                                size_hint=(None,None),size=(300,300))
                pop.open()
                self.email.text = ''
            
        else:
            invalidForm()
            self.email.text = ''      


    def logOut(self):
        sm.current = 'login'

class Admin(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text == 'admin' and self.password.text == 'admin':
            self.reset()
            sm.current = 'create'
        
        else:
            invalidLogin()
            self.email.text = ""
            self.password.text = ""

    def loginBtn(self):
        self.reset()
        sm.current = 'create'

    def logOut(self):
        sm.current = 'login'

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class Student(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class Teacher(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class Boss(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class Parent(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class Driver(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',title_align = 'center',title_color=(0,0,0,1),content=Label(text='Invalid username or password',color=(0,0,0,1)),background="photo/popup.jpg",
                    size_hint=(None,None),size=(300,300))

    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',title_align = 'center',title_color=(0,0,0,1),content=Label(text='Please fill in all inputs with valid information.',color=(0,0,0,1)),background="photo/popup.jpg",
                    size_hint=(None,None),size=(300,300))

    pop.open()

def invalidEmail():
    pop = Popup(title='Invalid Email',title_align = 'center',title_color=(0,0,0,1),content=Label(text='Email Not Detected, Please Check Email.',color=(0,0,0,1)),background="photo/popup.jpg",
                    size_hint=(None,None),size=(300,300))

    pop.open()

kv = Builder.load_file('admin.kv')
kv = Builder.load_file('loginwindow.kv')
kv = Builder.load_file('verifywindow.kv')
kv = Builder.load_file('completeinfo.kv')
kv = Builder.load_file('forgotpassword.kv')
kv = Builder.load_file('createaccountwin.kv')
kv = Builder.load_file('student.kv')
kv = Builder.load_file('teacher.kv')
kv = Builder.load_file('parent.kv')
kv = Builder.load_file('boss.kv')
kv = Builder.load_file('driver.kv')



sm = WindowManager()

screens =  [Admin(name='admin'),
            LoginWindow(name='login'), 
            VerifyWindow(name='verify'),
            Student(name='student'),
            Teacher(name='teacher'),
            Parent(name='parent'),
            Boss(name='boss'),
            Driver(name='driver'),
            CompleteInfo(name='complete'),
            ForgotPassword(name='forgot'),
            CreateAccountWindow(name='create')]
            
for screen in screens:
    sm.add_widget(screen)

sm.current = 'login'

class MySchoolApp(App):
    App.title = 'Welcome to MySchool'
    def build(self):
        return sm

if __name__ == '__main__':
    con = pymysql.connect('localhost','database username','password','myschool')
        
    MySchoolApp().run()
    con.close()
