from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (304, 480)

KV = """
MDScreen:
    name: "LoginPage"
    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: .6
            pos_hint: {"center_y": 1.2}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (0,.4,.8, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
        MDIconButton:
            id: icon
            icon: "account-circle"
            pos_hint: {"center_x": .5, "center_y": .8}
            user_font_size: "60sp"
            theme_text_color: "Custom"
            text_color: 0,.4,.8,1
        MDTextField:
            id: login 
            hint_text: "Enter Login Name"
            helper_text: "or click on forgot my name"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint_x:None
            width:200
        MDTextField:
            id: pin 
            hint_text: "Enter PIN"
            helper_text: "or click on forgot my PIN"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.4}
            size_hint_x:None
            width:200
        MDRaisedButton:
            text: "Login"
            pos_hint:{'center_x': 0.5, 'center_y': 0.25}
            size_hint_x: .5
            md_bg_color: 0,.4,.8,1
        
"""

class LoginApp(MDApp):

    def change_screen(self, name):
        screen_manager.current = LoginPage
    
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        
        return screen_manager

       

if __name__ == '__main__':
    app = LoginApp()
    app.run()