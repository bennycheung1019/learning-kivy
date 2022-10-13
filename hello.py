from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField

class HelloWorld(MDApp):
    def flip(self):
        print("working...")

    def build(self):
        screen = MDScreen()

        #topAppBar
        self.topAppBar= MDTopAppBar(title="i am title")
        self.topAppBar.pos_hint = {"top": 1}
        self.topAppBar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.topAppBar)

        #logo
        screen.add_widget(Image(source="logo.png",
        pos_hint = {"center_x": 0.5, "center_y": 0.7}
        ))

        #collect user input
        self.input = MDTextField(
            text = "enter a binary number",
            halign="center",
            size_hint = (0.8, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = 40
            )
        screen.add_widget(self.input)

        return screen

if __name__ == '__main__':
    HelloWorld().run()


