from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.core.window import Window
Window.size = (400, 750)

class TestPage(MDFloatLayout): # Screen "TestPage"
    pass

class testtemplateApp(MDApp): # design in testtemplate.kv the screen

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        
        

    def build(self):
        return TestPage() # read in the kv-file and build the screen

if __name__ == '__main__':
    app = testtemplateApp()
    app.run()