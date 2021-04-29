# https://www.youtube.com/watch?v=2ImbdfgY0Gg

from kivymd.app import MDApp
from kivy.lang import Builder

# color defined in https://www.w3schools.com/colors/colors_rgb.asp
helpstr = '''
MDScreen:
    md_bg_color: 1,.6,.3,1
    orientation: 'vertical'
    MDLabel:
        text:'Login'
        font_style : 'Button'
        font_size : 50
        halign : 'center'
        size_hint_y : None
        height: self.texture_size[1]
        pos_hint: {'center_y':0.65}
    MDTextFieldRound:
        hint_text : 'username'
        icon_right: 'account'
        helper_text: 'Required'
        size_hint_x : None
        width: 220
        font_size: 20
        color_active: [1,1,1,1]
        pos_hint: {'center_x':0.5,'center_y':0.55}
    MDTextFieldRound:
        hint_text : 'password'
        icon_right: 'eye-off'
        helper_text: 'Required'
        size_hint_x : None
        width: 220
        font_size: 20
        color_active: [1,1,1,1]
        password: True
        pos_hint: {'center_x':0.5,'center_y':0.45}
    MDRoundFlatButton:
        text: 'sign-up'
        pos_hint: {'center_x':0.5,'center_y':0.25}
        font_size: 20
'''

class MyApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng


MyApp().run()