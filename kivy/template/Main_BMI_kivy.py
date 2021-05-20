from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivy.core.window import Window
Window.size = (400, 750)


class Home2Screen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ChildHealthApp(MDApp):

    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        
        

    def build(self):
        return

if __name__ == '__main__':
    app = ChildHealthApp()
    app.run()