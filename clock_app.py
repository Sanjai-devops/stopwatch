from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from time import strftime
from kivy.clock import Clock
from kivy.lang import Builder


kv = """
<label>:
     font_name: 'Roboto'
     font_size: 60
     markup: True
<RobotoButton@Button>:
     background_color: (1,1,1,1)
     border: (2, 2, 2, 2)
     font_name: 'Roboto'
     font_size: 25
     bold: True

BoxLayout:
     orientation: 'vertical'

     Label:
          id: time
          text: '[b]00[/b]:00:00'
     BoxLayout:
          height: 90
          orientation: 'horizontal'
          padding: 20
          spacing: 20
          size_hint: (1, 0)

          RobotoButton:
               id: start_stop
               text: 'Start'
               on_press: app.start_stop()

          RobotoButton:
               id: reset
               text: 'Reset'
               background_color: (1,1,0,1)
               on_press: app.reset()
     Label:
          id: stopwatch
          text: '00:00.[size=40]00[/size]' 
"""


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def build(self):
        return Builder.load_string(kv)

    def update_time(self, val):
        if self.sw_started:
            self.sw_seconds += val
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = '%02d:%02d.[size=40]%02d[/size]' % \
                                       (int(minutes), int(seconds), int(seconds * 100 % 100))
        self.root.ids.time.text = strftime('[b]%H:[/b]%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = ('start' if self.sw_started else 'stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
