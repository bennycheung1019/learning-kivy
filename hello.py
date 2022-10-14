from tkinter import font
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton

class HelloWorld(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.topAppBar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state = 0
            self.topAppBar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
            self.converted.text = ""
            self.label.text = ""

    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text, 2)
            self.converted.text = str(val)
            self.label.text = "in decimal is:"
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = val
            self.label.text = "in binary is:"

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "DeepOrange"
        Window.size = [300, 600]
        screen = MDScreen()

        #topAppBar
        self.topAppBar= MDTopAppBar(title="Binary to Decimal")
        self.topAppBar.pos_hint = {"top": 1}
        self.topAppBar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.topAppBar)

        #logo
        screen.add_widget(Image(source="logo.png",
        pos_hint = {"center_x": 0.5, "center_y": 0.7},
        size_hint = (0.5, 1)
        ))

        #collect user input
        self.input = MDTextField(
            text = "enter a binary number",
            halign="center",
            size_hint = (0.8, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = '20sp'
            )
        screen.add_widget(self.input)

        #secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        screen.add_widget(self.label)

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.converted)

        # Convert Button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size = '17sp',
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.convert
        ))

        return screen

if __name__ == '__main__':
    HelloWorld().run()


