from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.base import EventLoop


class MainScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        Window.size = (250, 550)
        return Builder.load_file('My.kv')

    def on_start(self):
        # Bind the back button press to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, window, key, *args):
        # The 'key' value of 27 is the Android back button or 'Esc' key
        if key == 27:
            if self.root.ids.nav_drawer.state == "open":
                self.root.ids.nav_drawer.set_state("close")
                return True  # Prevent the app from closing
        return False  # Allow the app to close if no drawer is open


if __name__ == "__main__":
    MyApp().run()
