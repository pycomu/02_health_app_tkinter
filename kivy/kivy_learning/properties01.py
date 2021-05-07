from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Container(BoxLayout): # Screen in BoxLayout method
    text_input = ObjectProperty() # variable for text input inside class
    label_widget = ObjectProperty() # variable for adressing label widget inside class

    def change_label_text(self):
        self.label_widget.text = self.text_input.text # variables exchange their values



class myproperty1App(App): # main class to build the Screen, looking for myproperty1.kv file with definitions

    def build(self):
        return Container()


if __name__ == '__main__':
    myproperty1App().run()