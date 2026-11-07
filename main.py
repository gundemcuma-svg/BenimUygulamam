from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BenimUygulamam(App):
    def build(self):
        ekran = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        baslik = Label(
            text="BENİM İLK UYGULAMAM",
            font_size=25
        )

        buton = Button(
            text="MERHABA!",
            font_size=22
        )

        ekran.add_widget(baslik)
        ekran.add_widget(buton)

        return ekran

BenimUygulamam().run()
