# ======================================================================================================================================================#
# Created by Aaditya Raj#
import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
try:
    os.system("pip install pipenv")
except:
    pass
try:
    os.system("pip install Pipfile")
except:
    pass
# imported items
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import datetime as dt
import requests
import pandas as pd
from kivymd.uix.button import MDFlatButton
import face_recognition
import pyodbc

# mysql connection
try:
    #con = ms.connect(host="localhost", passwd="2306", user="root", database="gailpro")
    con = ms.connect(host="localhost", passwd="2306", user="root", database="gailpro")
    cur = con.cursor()
    db_conn = "Connected"
except:
    db_conn = "Not_Connected"

# internet connection




# main screen window size

Window.mainloop()
Window.size = (400, 700)
Window.top = 80
Window.left = 500

filestring = """
<UI>:
    name:'ui'
    MDScreen:
        name: "beforelogin"
        MDFloatLayout:
            md_bg_color:255/255 , 255/255 , 255/255 , 1
            Image:
                source: "images/GAIL1.jpg"
                pos_hint: {"center_x": .5 , "center_y": .5}
            MDLabel:
                text: "GAS AUTHORITY"
                pos_hint:{"center_x": .5 , "center_y": .53}
                halign:"center"
                theme_text_color: "Custom"
                text_color: 0/255 , 0/255 , 0/255 , .8
                font_size:"35sp"
                bold: True
                font_name:"Poppins-SemiBold"
            MDLabel:
                text: "OF INDIA LIMITED"
                pos_hint:{"center_x": .5 , "center_y": .47}
                halign:"center"
                theme_text_color: "Custom"
                text_color: 0/255 , 0/255 , 0/255 , .8
                font_size:"35sp"
                bold: True
                font_name:"Poppins-SemiBold"
            MDLabel:
                id:connectioncheck
                text:
                pos_hint:{"center_x": .5 , "center_y": .3}
                halign:"center"
                theme_text_color: "Custom"
                text_color: 220/255 ,22/255 , 18/255 , .8
                font_size:"25sp"
                bold: True
                font_name:"Poppins-SemiBold"

            MDTextButton:
                text:"Proceed To Login"
                theme_text_color: "Custom"
                text_color: 0,0,0.1/255,1
                font_size: "20sp"
                halign:"center"
                md_bg_color: 0,0,0,0.01
                font_name:"Poppins-Medium"
                size_hint: .6, .08
                pos_hint:{"center_x":.5,"center_y":.2}
                on_release: app.proceed()
                elevation:0
				
    MDScreen:
        name: "login"
        MDFloatLayout:
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "chevron-left"
                user_font_size:"40sp"
                pos_hint:{"center_x": 0.08,"center_y": .93}
                on_release: app.back_to_before_login()

            MDTextButton:
                text:"Back"
                font_size:"25sp"
                font_name: "Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint:{"center_x": .179 , "center_y": .932}
                on_release:app.back_to_before_login()

            Image:
                source: "images/GAIL3.png"
                size_hint: .6 , .4
                pos_hint:{"center_x":0.25,"center_y":0.77}

            MDLabel:
                text:"Proceed with your"
                font_size: "30sp"
                font_name:"Poppins-Medium"
                color: 0 , 0 , 0 , .6
                pos_hint: {"center_x":.553 , "center_y":.62}

            MDLabel:
                text:"Login"
                font_size: "40sp"
                font_name:"Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint: {"center_x":.553 , "center_y":.56}

            MDFloatLayout:
                size_hint: .7, .08
                pos_hint: {"center_x": .51, "center_y":.47}
                MDTextField:
                    id:username
                    hint_text:"Username"
                    max_text_length:8
                    required:True
                    helper_text:""
                    helper_text_mode:"on_error"
                    pos_hint:{"center_x":0.42,"center_y":0.5}
                    size_hint_x:None
                    width: 320
                    font_size:"20sp"
                    line_color_focus: 0,0,0,1
                    multiline:False
                MDIconButton:
                    icon:"account"
                    user_font_size:"20sp"
                    pos_hint:{"center_x": 1.05,"center_y": .5}
            MDFloatLayout:
                size_hint: .7, .08
                pos_hint: {"center_x": .51, "center_y":.38}
                MDTextField:
                    id:password
                    hint_text:"Password"
                    max_text_length:8
                    required:True
                    helper_text:""
                    helper_text_mode:"on_error"
                    pos_hint:{"center_x":0.42,"center_y":0.5}
                    size_hint_x:None
                    width: 320
                    font_size:"20sp"
                    line_color_focus: 0,0,0,1
                    multiline:False
                    password:True
                MDIconButton:
                    id: passbutt
                    icon:"eye"
                    user_font_size:"20sp"
                    pos_hint:{"center_x": 1.05,"center_y": .5}
                    on_release:app.viewpass()

            MDRaisedButton:
                text:"Click To Login"
                theme_text_color: "Custom"
                font_size: "20sp"
                text_color: 0,0,1/255 ,1
                halign:"center"
                font_name:"Poppins-Medium"
                size_hint: .88, .08
                pos_hint:{"center_x":.5,"center_y":.28}
                on_release: app.get_data()
                md_bg_color:235/255,49/255,54/255 , 1
            MDTextButton:
                id : quit
                text: "Quit"
                font_size:"25sp"
                font_name: "Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint:{"center_x": .135 , "center_y": .15}
                on_release:app.terminate()
            MDTextButton:
                text:"Clear"
                font_size:"18sp"
                font_name: "Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint:{"center_x": .5 , "center_y": .22}
                on_release: app.clear()
            MDLabel:
                id:date
                text:root.currdate
                font_size: "15sp"
                font_name:"Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint: {"center_x":1.23 , "center_y":.927}

    MDScreen:
        name: "insidepage"
        MDFloatLayout:
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "chevron-left"
                user_font_size:"40sp"
                pos_hint:{"center_x": 0.08,"center_y": .93}
                on_release: app.logout()
            MDTextButton:
                text:"Logout"
                font_size:"25sp"
                font_name: "Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint:{"center_x": .21 , "center_y": .932}
                on_release: app.logout()

            Image:
                source: "images/GAIL3.png"
                size_hint: .17 , .1
                pos_hint:{"center_x":0.64,"center_y":0.925}

            MDCard:
                size_hint: None, None
                size : 380 , 210
                md_bg_color: 1 , 1 , 1 ,1
                pos_hint: {"center_x": .5, "center_y":.73}
                elevation : 30
                padding: 15
                radius:15
                spacing:0
                focus_behavior:True
                ripple_behavior:True

                MDLabel:
                    id:nameofuser
                    text: ""
                    pos_hint:{"center_x":0.5,"center_y":0.98}
                    size_hint_x:None
                    width: 350
                    font_size:"22sp"
                    font_name:"Poppins-Italic"

            MDLabel:
                id:branch
                text: ""
                pos_hint:{"center_x":.5,"center_y":0.81}
                size_hint_x:None
                width: 350
                font_size:"20sp"
                font_name:"Poppins-Medium"

            MDLabel:
                id:city
                text:""
                pos_hint:{"center_x":.5,"center_y":0.775}
                size_hint_x:None
                width: 350
                font_size:"20sp"
                font_name:"Poppins-Medium"
            MDLabel:
                id:mobno
                text:""
                pos_hint:{"center_x":.5,"center_y":0.74}
                size_hint_x:None
                width: 350
                font_size:"20sp"
                font_name:"Poppins-Medium"

            MDLabel:
                id:mail
                text:""
                pos_hint:{"center_x":.5,"center_y":0.61}
                size_hint_x:None
                width: 350
                font_size:"13sp"
                font_name:"Poppins-Medium"


            MDTextButton:
                id : quit
                text: "Quit"
                font_size:"25sp"
                font_name: "Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint:{"center_x": .135 , "center_y": .15}
                on_release:app.terminate()

            MDLabel:
                id:date
                text:root.currdate
                font_size: "15sp"
                font_name:"Poppins-SemiBold"
                color: 0 , 0 , 0 , 1
                pos_hint: {"center_x":1.23 , "center_y":.927}

            Image:
                id: empimg
                source: "user.jpg"
                size_hint: .17 , .1
                pos_hint:{"center_x":.13,"center_y":0.675}

            MDRaisedButton:
                text:"Mark Attendance"
                md_bg_color:(116/255, 179/255, 247/255,1)
                theme_text_color: "Custom"
                font_size: "15sp"
                text_color: 0,0,1/255,1
                anchor_x:"center"
                anchor_y : "bottom"
                font_name:"Poppins-Medium"
                size_hint: .4, .26
                pos_hint:{"center_x":.225,"center_y":.4}
                line_color: (116/255, 179/255, 247/255,1)
                line_width: 1.5
                on_release:app.cam()
            Image:
                source:'images/camera.jpg'
                size_hint:.395,.35
                pos_hint:{"center_x":.2237,"center_y":0.414}
            MDRaisedButton:
                text:"View Attendance"
                md_bg_color:(116/255, 179/255, 247/255,1)
                theme_text_color: "Custom"
                font_size: "15sp"
                text_color: 0,0,1/255,1
                anchor_x:"center"
                anchor_y : "bottom"
                font_name:"Poppins-Medium"
                size_hint: .4, .26
                pos_hint:{"center_x":.775,"center_y":.4}
                line_color: (116/255, 179/255, 247/255,1)
                line_width: 1.5
                on_release:app.viewattendance()
            Image:
                source:'images/attendance.png'
                size_hint:.395,.35
                pos_hint:{"center_x":.7737,"center_y":0.414}



    MDScreen:
        name:"cam"
        MDFloatLayout:
            md_bg_color: 1,1,1,1
            Camera:
                id:camera
                resolution:(640,1280)
                size_hint_y: None
                pos: self.x, dp(48)
                height: root.height - dp(48)
                allow_stretch: True
                keep_ratio: True
                play: False
            MDRaisedButton:
                text:"Mark Attendance"
                md_bg_color:(1, 0, 0,.6)
                theme_text_color: "Custom"
                font_size: "15sp"
                text_color: 0,0,1/255,1
                anchor_x:"center"
                anchor_y : "center"
                font_name:"Poppins-Medium"
                size_hint: 1.0, .08
                pos_hint:{"center_x":.5,"center_y":.23}
                line_color: (1, 0, 0,1)
                line_width: 1.5
                on_release : app.verifyatten()
            MDRaisedButton:
                text:"Back"
                md_bg_color:(1, 0, 0,.6)
                theme_text_color: "Custom"
                font_size: "15sp"
                text_color: 0,0,1/255,1
                anchor_x:"center"
                anchor_y : "center"
                font_name:"Poppins-Medium"
                size_hint: 1.0, .08
                pos_hint:{"center_x":.5,"center_y":.14}
                line_color: (1, 0, 0,1)
                line_width: 1.5
                on_release:app.backcam()

    MDScreen:
        name : "atten"
        MDCard:
            size_hint: None, None
            size : 400 , 600
            md_bg_color: 1 , 1 , 1 ,1
            pos_hint: {"center_x": .49, "center_y":.52}
            elevation : 0
            padding: 15
            radius:0
            spacing:0
            focus_behavior:True
            ripple_behavior:False
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True

                MDLabel:
                    id:attst
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                    font_size:"20sp"
                    font_name: "Poppins-SemiBold"
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 5, 5
                    color: 0,0,0,1
                    text: ''
        MDTextButton:
            text: "Back"
            font_size:"25sp"
            font_name: "Poppins-SemiBold"
            color: 0 , 0 , 0 , 1
            pos_hint:{"center_x": .115 , "center_y": .08}
            on_release:app.root.current="insidepage"
        MDLabel:
            id:label
            text: ""
            font_size:"25sp"
            font_name: "Poppins-SemiBold"
            color: 0 , 0 , 0 , 1
            pos_hint:{"center_x": .55 , "center_y": .95}
"""
# main sceeen class with Screen Manager

class UI(ScreenManager):
    date = dt.datetime.now()
    currdate = f"{date:%d %b %Y}"


# main App and functions
class GailLogin(MDApp):
    # loads kivy file

    def build(self):
        Builder.load_string(filestring)
        self.icon = 'E:\\myproject\\images\\GAIL3.png'
        return UI()

    # ================================#
    # dialouge box

    def dilog(self, obj, diltxt):
        button_close = MDFlatButton(text='Close', on_release=self.close_dilog)
        self.dbox = MDDialog(title="Information", text=diltxt, buttons=[button_close])
        self.dbox.open()

    def close_dilog(self, obj):
        self.dbox.dismiss()

    # ==========================================#
    # proceed to login screen
    def proceed(self):
        url = "https://www.google.com"
        timeout = 5.
        try:
            request = requests.get(url, timeout=timeout)
            web_conn = "Connected"
        except:
            web_conn = "Not_Connected"
        if web_conn == "Connected" and db_conn == "Connected":
            self.root.current = "login"
        else:
            self.root.ids.connectioncheck.text = "No Connection!"

    # getting login info and login
    def get_data(self):
        self.username = self.root.ids.username.text
        userpass = self.root.ids.password.text

        try:
            cur.execute('select Username from emplinfo where Username = %s', (self.username,))
            fetched_data = cur.fetchall()
            if (self.username,) in fetched_data:
                cur.execute(
                    'select Username,Password,emp_name,mailid,branch,city,mobileno,empimg,empatt from emplinfo where Username = %s',
                    (self.username,))
                fetched_data = cur.fetchall()
                if self.username == fetched_data[0][0]:
                    if userpass == fetched_data[0][1]:
                        try:
                            os.remove("user1.jpg")
                        except:
                            pass
                        try:
                            os.remove('attensheet.accdb')
                        except:
                            pass
                        em = open("user1.jpg", "wb").write(fetched_data[0][7])
                        et = open('attensheet.accdb', 'wb').write(fetched_data[0][8])
                        self.root.ids.empimg.source = "user1.jpg"
                        self.root.ids.nameofuser.text = f"Welcome : {fetched_data[0][2]}"
                        self.root.ids.branch.text = f"Branch : {fetched_data[0][4]}"
                        self.root.ids.city.text = f"City : {fetched_data[0][5]}"
                        self.root.ids.mobno.text = f"My Number : {fetched_data[0][6]}"
                        self.root.ids.mail.text = f"My Mail ID : {fetched_data[0][3]}"
                        self.root.current = "insidepage"
                    else:
                        self.dilog(diltxt="Wrong Password", obj='')

                else:
                    self.dilog(diltxt="Wrong Username", obj='')
            else:
                self.dilog(diltxt="Wrong Username", obj='')
        except:
            self.dilog(diltxt="Something went Wrong", obj='')

    def back_to_before_login(self):
        self.root.current = "beforelogin"

    def logout(self):
        self.root.current = "login"
        self.root.ids.username.text = ""
        self.root.ids.password.text = ""
        try:
            os.remove("user1.jpg")
            os.remove("cam.png")
        except:
            pass

    def clear(self):
        self.root.ids.username.text = ""
        self.root.ids.password.text = ""

    def viewpass(self):
        if self.root.ids.password.password:
            self.root.ids.password.password = False
            self.root.ids.passbutt.icon = "eye-off"
        elif not self.root.ids.password.password:
            self.root.ids.password.password = True
            self.root.ids.passbutt.icon = "eye"

    def cam(self):
        self.root.ids.camera.play = True
        self.root.current = 'cam'

    # dialouge for camera verify
    # ======#
    def attnverified(self, obj):
        okay = MDFlatButton(text='Okay', on_release=self.attnverifieddismiss)
        self.dbox1 = MDDialog(title="Information", text="Attendance verified", buttons=[okay])
        self.dbox1.open()

    def attnverifieddismiss(self, obj):
        self.root.current = "insidepage"
        self.root.ids.camera.play = False
        self.dbox1.dismiss()

    def attnnotverified(self, obj):
        button_retry = MDFlatButton(text='Retry', on_release=self.attnnotverifieddismiss)
        button_back = MDFlatButton(text='Back', on_release=self.attnverifieddismiss)
        self.dbox1 = MDDialog(title="Information", text="Attendance not verified", buttons=[button_retry, button_back])
        self.dbox1.open()

    def attnnotverifieddismiss(self, obj):
        self.dbox1.dismiss()

    def somethingwentwrong(self, obj):
        button_back = MDFlatButton(text='Back', on_release=self.attnverifieddismiss)
        self.dbox1 = MDDialog(title="Information", text="Attendance not verified", buttons=[button_back])
        self.dbox1.open()

    def attenalreadymarkeddismiss(self, obj):
        os.remove('attensheet.accdb')
        self.dbox1.dismiss()
        self.stop()

    def attenalreadymarked(self, obj):
        butt_reback = MDFlatButton(text = "Back" , on_release = self.attnverifieddismiss)
        button_back = MDFlatButton(text='Quit', on_release=self.attenalreadymarkeddismiss)
        self.dbox1 = MDDialog(title="Information", text="Attendance already marked", buttons=[button_back , butt_reback])
        self.dbox1.open()

    # ====#
    def verifyatten(self):
        camera = self.root.ids['camera']
        camera.export_to_png("cam.png")
        # face recon
        try:
            known_image = face_recognition.load_image_file("user1.jpg")
            unknown_image = face_recognition.load_image_file("cam.png")

            user_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            results = face_recognition.compare_faces([user_encoding], unknown_encoding)
            if results == [True]:
                try:
                    dat = dt.datetime.now()
                    day = dat.strftime('%A')  # day
                    date = f'{dat:%d-%b-%Y}'
                    mnth = f'{dat:%B}'
                    time = f'{dat:%H:%M}'
                    cwd = os.getcwd()
                    cwd = cwd + '\\attensheet.accdb'
                    at_con = 'DRIVER={};DBQ={};'.format('{Microsoft Access Driver (*.mdb, *.accdb)}', cwd)
                    con_at = pyodbc.connect(at_con)
                    cur_at = con_at.cursor()
                    cur_at.execute("insert into attendancesheet values(? ,? ,?,?,? )",
                                   (date, day, time, 'Present', mnth))
                    cur_at.commit()
                    datasheet = open('attensheet.accdb', 'rb').read()
                    cur.execute('update emplinfo set empatt = %s where username = %s', (datasheet, self.username))
                    con.commit()
                    self.attnverified(obj='')

                except:
                    self.attenalreadymarked(obj='')

            else:
                print("not verified")
                os.remove('cam.png')
                self.attnnotverified(obj='')
        except:
            self.somethingwentwrong(obj='')

    def backcam(self):
        self.root.ids.camera.play = False
        self.root.current = 'insidepage'

    def viewattendance(self):
        dat = dt.datetime.now()
        mnth = f'{dat:%B}'
        cwd = os.getcwd()
        cwd = cwd + '\\attensheet.accdb'
        at_con = 'DRIVER={};DBQ={};'.format('{Microsoft Access Driver (*.mdb, *.accdb)}', cwd)
        con_at = pyodbc.connect(at_con)
        cur_at = con_at.cursor()
        cur_at.execute('Select attendate from attendancesheet where mnth = ?', (mnth,))
        attendata = cur_at.fetchall()
        attstr = ''
        for i in range(0, len(attendata)):
            attstr = attstr + attendata[i][0] + '      Present' + '\n'
        self.root.ids.attst.text = attstr
        self.root.ids.label.text = f'Attendance of - {mnth}'
        self.root.current = 'atten'

    def terminate(self):
        try:
            os.remove("user1.jpg")
        except:
            pass
        try:
            os.remove('attensheet.accdb')
        except:
            pass
        try:
            os.remove('cam.png')
        except:
            pass
        self.stop()

    def on_stop(self):
        try:
            os.remove("user1.jpg")
        except:
            pass
        try:
            os.remove('attensheet.accdb')
        except:
            pass
        try:
            os.remove('cam.png')
        except:
            pass


if __name__ == "__main__":
    GailLogin().run()
