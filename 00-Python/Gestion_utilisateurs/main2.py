import json
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.image import Image


class RootLayout(BoxLayout):
    def __init__(self, **kwargs):
        self.size = (Config.get('graphics', 'width'), Config.get('graphics', 'height'))
        super().__init__(**kwargs)
        self._currentWindow = None
        self._user = None
        self.changeWindow("Connexion")

    def changeWindow(self, str):
        if self._currentWindow is not None:
            self.remove_widget(self._currentWindow)
        if str == "Images":
            self._currentWindow = ImagesLayout()
        elif str == "Connexion":
            self._currentWindow = ConnexionLayout(pos_hint={"x": 0, "y": 0}, size_hint=(1, 1))
        if self._currentWindow is not None:
            self.add_widget(self._currentWindow)
            self._currentWindow.set_parent(self)

    def set_user(self, v):
        self._user = v


class ConnexionLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._parent = None
        self._surname = None
        self._name = None
        self._age = None
        self._labels = []
        self.createLabels()
        self._textInputs = []
        self.createTextInputs()
        self._connexionButton = self.createButton(self, "Connexion", 0, 0, .5, .2)
        self._registerButton = self.createButton(self, "Register", .5, 0, .5, .2)
        self._stored_users = []
        self.getStored_users()

    def set_surname(self, str):
        self._surname = str

    def set_name(self, str):
        self._name = str

    def set_age(self, int):
        self._age = int

    def name(self):
        return self._name

    def surname(self):
        return self._surname

    def age(self):
        return self._age

    def stored_users(self):
        return self._stored_users

    def set_stored_users(self, infos):
        self._stored_users = infos

    def add_stored_users(self, infos):
        self._stored_users.append(infos)

    def set_parent(self, instance):
        self._parent = instance

    def createLabels(self):
        self._labels.append(self.createLabel(parent=self, text="Nom : ", x=0, y=0.8, width=0.5, height=0.2))
        self._labels.append(self.createLabel(parent=self, text="Prénom : ", x=0, y=0.6, width=0.5, height=0.2))
        self._labels.append(self.createLabel(parent=self, text="Âge : ", x=0, y=0.4, width=0.5, height=0.2))

    def createLabel(self, parent, text: str, x: float, y: float, width: float, height: [float, None]):
        label = Label(text=text, pos_hint={"x": x, "y": y}, size_hint=(width, height))
        parent.add_widget(label)
        return label

    def createTextInputs(self):
        self._textInputs.append(self.createTextInput(self, .5, .8, .5, .2))
        self._textInputs.append(self.createTextInput(self, .5, .6, .5, .2))
        self._textInputs.append(self.createTextInput(self, .5, .4, .5, .2, int=True))

    def createTextInput(self, parent, x: float, y: float, width: float, height: float, int=False):
        if int:
            textInput = TextInput(size_hint=(width, height), pos_hint={"x": x, "y": y}, input_filter='int')
        else:
            textInput = TextInput(size_hint=(width, height), pos_hint={"x": x, "y": y})
        textInput.bind(text=self.setInfo)
        parent.add_widget(textInput)
        return textInput

    def createButton(self, parent, name: str, x: float, y: float, width: float, height: float):
        button = Button(text=name, pos_hint={"x": x, "y": y}, size_hint=(width, height))
        if name == "Connexion":
            button.bind(on_press=self.login)
        elif name == "Register":
            button.bind(on_press=self.register)
        parent.add_widget(button)
        return button

    def setInfo(self, instance, str):
        tIndex = self._textInputs.index(instance)
        if tIndex == 0:
            self.set_surname(str)
        elif tIndex == 1:
            self.set_name(str)
        elif tIndex == 2:
            self.set_age(str)

    def getStored_users(self):
        try:
            with open("users.json", 'r') as f:
                jsonDict = json.load(f)
                for key, value in jsonDict.items():
                    self.add_stored_users([value["Nom"], value["Prénom"], value["Âge"]])
        except FileNotFoundError:
            pass

    def login(self, instance):
        if "" not in self._textInputs:
            try:
                with open("users.json", 'r') as f:
                    jsonDict = json.load(f)
                    for key, value in jsonDict.items():
                        for user in self.stored_users():
                            if user == [value["Nom"], value["Prénom"], value["Âge"]] == [self.surname(), self.name(),
                                                                                         self.age()]:
                                [self.remove_widget(w) for w in self._labels]
                                [self.remove_widget(w) for w in self._textInputs]
                                self.remove_widget(self._connexionButton)
                                self.remove_widget(self._registerButton)
                                self._parent.set_user(key)
                                self._parent.changeWindow("Images")
                                return
            except FileNotFoundError:
                pass
            finally:
                print("Could not login.")

    def register(self, instance):
        self.add_stored_users([self.surname(), self.name(), self.age()])
        with open("users.json", "w") as f:
            registerInfo = {}
            for i in range(len(self.stored_users())):
                st = self.stored_users()
                registerInfo[i] = {"Nom": st[i][0], "Prénom": st[i][1], "Âge": st[i][2]}
            json.dump(registerInfo, f, indent=4, ensure_ascii=False)
        print("Registered!")


class ImagesLayout(FloatLayout):
    def __init__(self, **kwargs):
        self.size = (Config.get('graphics', 'width'), Config.get('graphics', 'height'))
        super().__init__(**kwargs)
        self._parent = None
        self._backButton = self.createButton(self, "Back", 0, .9, .1, .1)
        self._image = 0
        self._imageWidget = None
        Clock.schedule_once(callback=self.nextImage)
        Clock.schedule_interval(callback=self.nextImage, timeout=3)

    def image(self):
        return self._image

    def set_image(self, img):
        self._image = img

    def set_parent(self, instance):
        self._parent = instance

    def createButton(self, parent, name: str, x: float, y: float, width: float, height: float):
        button = Button(text=name, pos_hint={"x": x, "y": y}, size_hint=(width, height))
        button.bind(on_press=self.go_back)
        parent.add_widget(button)
        return button

    def go_back(self, instance):
        self.remove_widget(self._imageWidget)
        self.remove_widget(self._backButton)
        Clock.stop_clock()
        self._parent.changeWindow("Connexion")
        return

    def nextImage(self, instance):
        if self.image() > 2:
            self.set_image(0)
        else:
            self.set_image(self.image() + 1)
        self.showImage(self.image())

    def set_imageWidget(self, img):
        self._imageWidget = img

    def showImage(self, imgId):
        if self._imageWidget is not None:
            self.remove_widget(self._imageWidget)
        self.set_imageWidget(Image(source=str(imgId)+".jpg"))
        self.add_widget(self._imageWidget)



class MyApp(App):
    def build(self):
        self.title = "Exo 2"
        return RootLayout()


def setConfig():
    Config.set('graphics', 'minimum_height', 200)
    Config.set('graphics', 'minimum_width', 200)
    Config.set('graphics', 'height', 720)
    Config.set('graphics', 'width', 1280)
    Config.set('graphics', 'resizable', 1)
    Config.set('graphics', 'fullscreen', 0)
    Config.write()


if __name__ == '__main__':
    setConfig()
    MyApp().run()
