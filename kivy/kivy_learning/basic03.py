from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder # required to have screen definition inside py file

# screen definition
page = '''
Screen:
    GridLayout:
        cols: 2
        Label:
            text: "User Name 3"
            font_size: 30
        TextInput:
            multiline: False
            font_size: 30
        Label:
            text: "password 3"
            font_size: 30
        TextInput:
            password: True
            multiline: False
            font_size: 30
'''


class basic3App(App): # main class to build the Login Screen
    def build(self):
        self.login = Builder.load_string(page) # read in screen definition above
        return self.login
    


if __name__ == '__main__':
    basic3App().run()