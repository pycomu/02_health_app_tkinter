# https://www.youtube.com/watch?v=3GBNMBhm6UU

from kivymd.app import App
from kivy.uix.boxlayout import BoxLayout


class my_boxlayout(BoxLayout): # defines the layout of screen and includes callback functions like "pushed"
    def pushed(self, clicked_now):
        output = "You clicked the " + clicked_now + " button."
        self.ids.result.text = output
        
    
class myApp(App):   # kv file must be named as "myApp" then
    def build(self):
        return my_boxlayout() # returns the rendering of class "my_boxlayout"

       

if __name__ == '__main__':
    myApp().run() # runnung the class myApp
    