import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock 
from kivy.core.audio import SoundLoader
import random

class boxx(FloatLayout):
    def __init__(self, **kwargs):
        super(boxx, self).__init__(**kwargs)

        self.opened = Image(source='pics/open.png', fit_mode='contain', size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        self.closed = Image(source='pics/close.png', fit_mode='contain', size_hint=(1, 1), allow_stretch=True, keep_ratio=True)

        self.bind(on_touch_down=self.shout)

        self.add_widget(self.closed)
        self.add_widget(self.opened)
        self.closed.opacity = 1
        self.opened.opacity = 0
        
    def open_mouth(self):
        self.opened.opacity = 1
        self.closed.opacity = 0
        
    def close_mouth(self, instance):
        self.closed.opacity = 1
        self.opened.opacity = 0

    def shout(self, instance, touch):
        self.open_mouth()
        number = random_integer = random.randint(0, 17)
        numb_to_str = str(number)
        exclaim = SoundLoader.load('sounds/' + numb_to_str + '.mp3')
        exclaim.play()
        Clock.schedule_once(self.close_mouth, exclaim.length)

            


class everything(App):

    def build(self):
        return boxx()

aboba = everything()
if __name__ == '__main__':

    aboba.run()
