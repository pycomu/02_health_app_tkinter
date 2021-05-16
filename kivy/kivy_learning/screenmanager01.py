from kivymd.app import MDApp
from kivy.lang import Builder # required to have screen definition inside py file
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (375, 750)

# screen definition
page = '''
ScreenManager:
    window_1:
    window_2:
        
<window_1>:
    id: "win1"
    
    MDButton:
        
        text:"Window 1"
        font_size: 30
        on_release: 
            root.manager.current = "win2"
             
<window_2>:
    id: "win2"
    MDButton:
        text: "Window 2"
        font_size: 30
        on_release:
            root.manager.current = "win1"
            
'''        

class window_1(Screen):
    pass

class window_2(Screen):
    pass

ms = ScreenManager()
ms.add_widget(window_1(name='win1'))
ms.add_widget(window_2(name='win2'))

class screenmanager1App(MDApp): # main class to build the Screen

    def build(self):
        self.scrmanager = Builder.load_string(page) # read in screen definition above
        return self.scrmanager


if __name__ == '__main__':
    screenmanager1App().run()