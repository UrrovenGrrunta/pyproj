from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from screens import HomeScreen, SettingsScreen


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"

        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/settings.kv")

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm


MyApp().run()