#!python

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.clock import Clock

__all__ = ('EditableLabel', ) #list of public modules

class EditableLabel(Label):

    edit = BooleanProperty(False)

    textinput = ObjectProperty(None, allownone=True)

    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos) and not self.edit:
            self.edit = True

        return super(EditableLabel, self).on_touch_down(touch)

    def on_edit(self, instance, value):

        if not value:
            if self.textinput:
                self.remove_widget(self.textinput)
            return

        self.textinput = t = TextInput(
                text=self.text, size_hint=(None, None),
                font_size=self.font_size, font_name=self.font_name,
                pos=self.pos, size=self.size, multiline=False)
        self.bind(pos=t.setter('pos'), size=t.setter('size'))
        self.add_widget(self.textinput)
        t.bind(on_text_validate=self.on_text_validate, focus=self.on_text_focus)
        Clock.schedule_once(lambda dt: self.textinput.cancel_selection())

    def on_text_validate(self, instance):
        self.text = instance.text
        self.edit = False

    def on_text_focus(self, instance, focus):
        if focus is False:
            self.text = instance.text
            self.edit = False
