from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout): # definition of screen in gridlayout method
    pass
            


class My2App(App): # main class to build the Login Screen, looking for my2.kv file with definitions

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    My2App().run()