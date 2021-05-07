from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout): # definition of screen in gridlayout method
    pass
            


class basic2App(App): # main class to build the Login Screen, looking for basic2.kv file with definitions

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    basic2App().run()