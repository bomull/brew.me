from kivy.app import App
import time
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from kivy.utils import get_color_from_hex
from kivy.base import EventLoop
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import beerxml_parser as bxml
from random import randint



class MaltRV(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fermentables = bxml.malts('grain.xml')

        self.data = [{"text": x['NAME']} for x in fermentables if 'NAME' in x]


class RVLabel(RecycleDataViewBehavior, Label):
    def on_press(self):
        self.ids.malt_info.text = str(randint(0,10))
        print ('pressed')


class ImageButton(ButtonBehavior, Image):
    pass

'''
class Namebutton(Widget):
    font_size = NumericProperty(24)
    nametext = NumericProperty(2)  # Text on tile
    color = ListProperty(get_color_from_hex('776E65'))
    text_color = ListProperty(get_color_from_hex('776E65'))

    def __init__(self, number=2, **kwargs):
        super(Namebutton, self).__init__(**kwargs)
        self.font_size = 0.5 * self.width
        self.number = number
        # self.update_text()

    def on_touch_down(self, touch):

        if self.parent is not EventLoop.window:
            return

        try:
            touch.push()
            self.transform_touch(touch)
            self._touch_diff = self.top - touch.y
            if self.collide_point(*touch.pos):
                FocusBehavior.ignored_touch.append(touch)
            return super(Namebutton, self).on_touch_down(touch)
        finally:
            touch.pop()

    def update_text(self, arg):
        pass

    def resize(self, arg):
        pass
'''

class BrewtalApp(App):

    def update_time(self, nap):
        self.root.ids.time.text = time.strftime('[b]%H[/b]:%M:%S') #access time using ID

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1) # call method update time with nap as argument

if __name__ == "__main__":
    BrewtalApp().run()
