from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Example of MDDialog App'
        font_style: 'H4'
        halign: "center"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Enter you password (123)'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True
        
    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.auth()
            
    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 1.0, 'center_y': 0.2}
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)

    # after pushing "Submit"
    def auth(self): 
        if self.root.in_class.text == '123': # password correct ? -> 123
            label = self.root.ids.show
            label.text = "Sucess" # set label at bottom
            # open popup dialog window
            self.dialog = MDDialog(title='Password check',
                                   text="Sucess !", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='More')] # more button no action linked
                                   )
            self.dialog.open()
        else:
            label = self.root.ids.show
            label.text = "Fail" # set label at bottom
            # open popup dialog window
            self.dialog = MDDialog(title='Password check',
                                   text="Fail !", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)])
            self.dialog.open()
            

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.root.in_class.text = "" # reset input field
        self.root.ids.show.text = "" # reset label at bottom


Main().run()