from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout): # definition of screen in gridlayout method

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) # overwriting exitsting class and adding new attributes
        self.cols = 2
        self.add_widget(Label(text='User Name 1', font_size = 30))
        self.username = TextInput(multiline=False, font_size = 30)
        self.add_widget(self.username)
        self.add_widget(Label(text='password 1', font_size = 30))
        self.password = TextInput(password=True, font_size = 30, multiline=False)
        self.add_widget(self.password)


class basic1App(App): # main class to build the Login Screen

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    basic1App().run()