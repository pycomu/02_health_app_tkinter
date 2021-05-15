# https://generalistprogrammer.com/python/python-app-development-for-beginners-kivy-mobile-app-tutorial/
# https://www.youtube.com/watch?v=Kcv1T6B7FEE&list=PLb9xOik0gj6pEPqB1baMISsSJU1nCm922&index=4
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
import requests
# import json
import uuid

Builder.load_string("""
<LoginScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        GridLayout:
            rows: 3
            cols: 1
            padding: 10
            spacing: 10
            row_default_height: 30
            MDTextField:
                hint_text: "Email"
                id: usernamevalue
            MDTextField:
                hint_text: "Password"
                id: passwordvalue
                password: True
            MDRectangleFlatButton:
                text: 'Login'
                on_press: root.login_button_action()

<FailedLoginScreen>
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Login Failed"
        MDRectangleFlatButton:
            text: 'Back To Login'
            on_press: root.manager.current = 'login'

<TaskScreen>
    ScrollView:
        MDList:
            id: tasklist
    MDFloatingActionButton:
        icon: "plus"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'addtaskscreen'  

<AddTaskScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        GridLayout:
            rows: 3
            cols: 1
            padding: 10
            spacing: 10
            row_default_height: 30
            MDTextField:
                hint_text: "Task Name"
                id: taskname
            MDRectangleFlatButton:
                text: 'Add Task'
                on_press: root.add_task()

<ListItemWithCheckbox>
    IconLeftWidget:
        icon: root.icon
    RightCheckbox:       

""")


db = JsonStore("tasks.json")


class LoginScreen(Screen):
    def build(self):
        pass
        
    def login_button_action(self):
        self.manager.current = 'taskscreen'
    
    # start - for API only
    # def login_button_action2(self): # to use in case of an API only
    #     url = 'https://reqres.in/api/login'
        
    #     #data = json.dumps({"email": "eve.holt@reqres.in","password": "cityslicka"})
    #     data = json.dumps({"email": self.ids.usernamevalue.text,"password": self.ids.passwordvalue.text})

    #     response = requests.post(url, data=data, headers={'Content-Type':'application/json'})

    #     userdata = json.loads(response.text)

    #     if userdata.get("token"):
    #         self.manager.current = 'tasklist'
    #     else:
    #         self.manager.current = 'failedlogin'
    # end - for API only



class FailedLoginScreen(Screen):
    def build(self):
        pass

class TaskScreen(Screen):
    def on_pre_enter(self):
        self.ids.tasklist.clear_widgets()
        for key,item in db.find():
            self.ids.tasklist.add_widget(ListItemWithCheckbox(text=f"{item.get('name')}",icon='pen'))

class AddTaskScreen(Screen):
    def add_task(self):
        db.put(uuid.uuid1().int, name= self.ids.taskname.text)    
        self.manager.current = 'taskscreen'


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass



class MainApp(MDApp):

    def build(self):
        self.title = "Task Manager"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(FailedLoginScreen(name='failedlogin'))
        sm.add_widget(TaskScreen(name='taskscreen'))
        sm.add_widget(AddTaskScreen(name='addtaskscreen'))
        return sm

if __name__ == '__main__':
    MainApp().run()