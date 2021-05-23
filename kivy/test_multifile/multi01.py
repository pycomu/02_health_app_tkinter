
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

class Multi01(BoxLayout):
    
    def callback(self):
        self.ids.label_text.text = "you pressed a key"

