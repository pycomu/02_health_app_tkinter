from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
# from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView

KV = '''
MDScreen:
    MDGridLayout:
        cols: 1
        text_input: text_input

        MDTextField:
            id: text_input 
            hint_text: "Enter message here"
            #pos_hint:{'center_x': 0.5, 'center_y': 0.9}
            #size_hint_x: .8
            text: ""
            
        
        MDRaisedButton:
            text: "Send message"
            #pos_hint:{'center_x': 0.5, 'center_y': 0.8}
            size_hint_x: 1
            md_bg_color: 0,.4,.8,1
            on_release: app.add_item()

        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            #pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            MDList:                
                id: message_list
                
'''


class Chatbot(MDApp):
    text_input = ObjectProperty()

    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        self.root.ids.message_list.add_widget(OneLineListItem(text=f"Bot:   It's my message, input your text above",
        bg_color = (.8,.8,.8,1)))

    def add_item(self):
        self.root.ids.message_list.add_widget(OneLineListItem(text= "You:   " + self.root.ids.text_input.text))
        self.root.ids.text_input.text = "" # reset input field
        self.root.ids.message_list.add_widget(OneLineListItem(text=f"Bot:   It's again your turn !",
        bg_color = (.8,.8,.8,1)))
        
if __name__ == '__main__':
    Chatbot().run()