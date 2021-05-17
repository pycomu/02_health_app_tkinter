import kivy
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
Window.size = (320, 600)

class MainApp(MDApp): 
    
    def build(self):
        ''' Initializes the Application and returns the root widget'''
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = "WhatsApp"

MainApp().run()

# Color 
# ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, 
# ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, 
# ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray.

# Hue
# range from 50 to A700.
# ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.
