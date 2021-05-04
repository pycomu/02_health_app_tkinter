from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (380, 600)

KV = """
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Food Info Page"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "food_info"
                
                

            OneLineListItem:
                text: "BMI Tracker"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "bmi_tracker"
Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        md_bg_color: 0,.4,.8,1
        elevation: 10
        title: "HappyChild"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "food_info"

                MDLabel:
                    text: "Food Info Page"
                    halign: "center"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
                MDTextField:
                    id: food_search 
                    hint_text: "Enter Food Name"
                    helper_text: "what food you want to look up?"
                    helper_text_mode: "on_focus"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x:None
                    width:200
                MDRaisedButton:
                    text: "Search"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: .5
                    md_bg_color: 0,.4,.8,1
                GridLayout:
                    rows: 1
                    size_hint: 1, .1
                    pos_hint: {"top": .1, "right": 1}
                    MDRaisedButton:
                        text: "BMI Track"
                        md_bg_color: 0,.4,.8,1
                        canvas.before:
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        markup: True                       
                        

            Screen:
                name: "bmi_tracker"
                
                MDLabel:
                    text: "BMI Tracker"
                    halign: "center"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
                MDTextField:
                    id: child_name 
                    hint_text: "Enter Child Name"
                    helper_text: "choose your child"
                    helper_text_mode: "on_focus"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x:None
                    width:200
                MDTextField:
                    id: height 
                    hint_text: "Enter child height"
                    helper_text: "Enter in meter"
                    helper_text_mode: "on_focus"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:200
                MDTextField:
                    id: weight 
                    hint_text: "Enter child weight"
                    helper_text: "Enter in Kg"
                    helper_text_mode: "on_focus"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                    size_hint_x:None
                    width:200
                MDLabel:
                    id: bmi_result
                    text: "The BMI calculated is :"
                    halign: "center"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.3}
                MDRaisedButton:
                    id: submit_bmi
                    text: "Submit"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                        
                    md_bg_color: 0,.4,.8,1
                GridLayout:
                    rows: 1
                    size_hint: 1, .1
                    pos_hint: {"top": .1, "right": 1}
                    MDRaisedButton:
                        text: "Food Info"
                        md_bg_color: 0,.4,.8,1
                        canvas.before:
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        markup: True  
                    


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

"""
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Happychild(MDApp):


    def build(self):
        
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = Happychild()
    app.run()

    # Consider the code below:

# <MyWidget>:
#     Button:
#         text: "Hello world, watch this text wrap inside the button"
#         text_size: self.size
#         font_size: '25sp'
#         markup: True
#     Button:
#         text: "Even absolute is relative to itself"
#         text_size: self.size
#         font_size: '25sp'
#         markup: True
#     Button:
#         text: "Repeating the same thing over and over in a comp = fail"
#         text_size: self.size
#         font_size: '25sp'
#         markup: True
#     Button:
# Instead of having to repeat the same values for every button, we can just use a template instead, like so:

# <MyBigButton@Button>:
#     text_size: self.size
#     font_size: '25sp'
#     markup: True

# <MyWidget>:
#     MyBigButton:
#         text: "Hello world, watch this text wrap inside the button"
#     MyBigButton:
#         text: "Even absolute is relative to itself"
#     MyBigButton:
#         text: "repeating the same thing over and over in a comp = fail"
#     MyBigButton:
# This class, created just by the declaration of this rule, inherits from the Button class and allows us to change default values and create bindings for all its instances without adding any new code on the Python side.