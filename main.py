from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get users string input from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        # Download the image
        req = requests.get(image_link)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widgets
        self.manager.current_screen.ids.img.source = imagepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
