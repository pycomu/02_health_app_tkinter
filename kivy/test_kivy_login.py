# https://www.youtube.com/watch?v=YjkllJYM3B0&list=PLjuHXsDGkbTQTAxdw2yJGAyFssmbaGKA1&index=6
# https://pastebin.com/4JqceyKm


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
 
Window.size = (1000,700)
 
Builder.load_string("""
<Login>
    ben: benName.text
    pw: passwort.text
    knopf: btn
 
    GridLayout:
        cols: 1
        size: root.width,root.height
        GridLayout:
            cols: 2
            Label:
                text: "Benutzername"
                font_size: 30
            TextInput:
                id: benName
                multiline: False
                font_size: 30
            Label:
                text: "Passwort"
                font_size: 30
            TextInput:
                password: True
                id: passwort
                multiline: False
                font_size: 30
        Button:
            size_hint: (1.,0.5)
            text:"anmelden"
            id: btn
            font_size: 30
            on_release: 
                root.loginPopup()
                root.manager.current = "geheim" if passwort.text == "1234" and benName.text == "Python" else "login"
                root.manager.transition.direction = "left"
 
<geheimerBereich>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Geheimer Bereich"
            font_size: 30
        Button:
            text: "zurück"
            font_size: 30
            on_release:
                root.manager.current = "login"
                root.manager.transition.direction = "right"
 
 
""")
 
class Login(Screen):
    ben = StringProperty()
    pw = StringProperty()
    knopf = ObjectProperty()    
    def loginPopup(self):
        if self.ben == "" or self.pw == "":
            popup = Popup(title='Fehler',
            content = Label(text="Es wurde kein Passwort oder Benutzername eingegeben!"),
            size_hint=(None,None),size=(400,400))
            popup.open()
        else:
            if self.ben == "Python" and self.pw == "1234":
                self.knopf.background_color = [0.,1.,0.,1.]
            else:
                self.knopf.background_color = [1.,0.,0.,1.]
 
class geheimerBereich(Screen):
    pass
 
ms = ScreenManager()
ms.add_widget(Login(name='login'))
ms.add_widget(geheimerBereich(name='geheim'))
 
class StartApp(App):
    def build(self):
        return ms
 
if __name__ == "__main__":
    StartApp().run()