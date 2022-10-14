# Learn Kivy using VScode

<a name=""></a>
## Setup Python
Install Python from [python.org](https://www.python.org/downloads/).

In terminal, create a directory on destkop

```
cd desktop
mkdir helloWorld
cd  helloWorld
```
to see if python is installed

```
python3 --version
```
to create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```
to open with VScode

```
code .
```
<a name="makeDirectory"></a>
## Setup Kivy using Pip
upgrade pip to the latest version

```
python -m pip install --upgrade pip
```
install kivy with kivy_example (optional)

```
python -m pip install "kivy[base]" kivy_examples
```
check what are installed

```
pip freeze
```
to checkout the example

```
python venv/share/kivy-examples/demo/showcase/main.py
```
## Setup Kivymd using Pip
install kivymd

```
pip install kivymd

```
## Starter code

```
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class HelloWorld(MDApp):
    def build(self):
        screen = MDScreen()
        return screen

if __name__ == '__main__':
    HelloWorld().run()

```

##Setup code . to open VScode

open `commend palette`  in VScode, type  `install code`
now `code .` will work



##Connect Github



## Kivymd Icons Preview
copy these code, save a .py file and run from terminal

```
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem


Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>

    IconLeftWidget:
        icon: root.icon


<PreviousMDIcons>

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()
```
```
python preview.py
```
## TopAppBar

```
from kivymd.uix.toolbar import MDTopAppBar

...

	self.topAppBar= MDTopAppBar(title="i am title")
	self.topAppbar.pos_hint = {"top": 1}
	self.topAppBar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
	screen.add_widget(self.topAppBar)

```

##Add logo

```
from kivy.uix.image import Image

...

#logo
    screen.add_widget(Image(source="logo.png",
    pos_hint = {"center_x": 0.5, "center_y": 0.7}
    ))
```

##Add Textfield

```
from kivymd.uix.textfield import MDTextField

...

#collect user input
    self.input = MDTextField(
        text = "enter a binary number",
        halign="center",
        size_hint = (0.8, 1),
        pos_hint = {"center_x": 0.5, "center_y": 0.5},
        font_size = 40
        )
    screen.add_widget(self.input)
```

##Add Labels

```

 #secondary + primary labels
        self.label = MDLabel(
            text="in decimal is:",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        screen.add_widget(self.label)

        self.converted = MDLabel(
            text="888",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.converted)
```

##Add button

```
from kivymd.uix.button import MDFillRoundFlatButton


# Convert Button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size = '17sp',
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.convert
        ))
```

##Add CONVERT function for the button
Button function always need 2 args

```
def convert(self, args):
        val = int(self.input.text, 2)
        self.converted.text = str(val)
```

##Remove initial labels 
Remove the following 2 lines 

```
 text="in decimal is:",
 text="888",
```

add to the convert function

```
self.label.text = "in decimal is:"

```

##add States 
add `self.state` under `build` function

```
def build(self):
        self.state = 0
```
and rewrite `flip` function

```
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
```
also rewirte `convert` function

```
 if self.state == 0:
            val = int(self.input.text, 2)
            self.converted.text = str(val)
            self.label.text = "in decimal is:"
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = val
            self.label.text = "in binary is:"
```