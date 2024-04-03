from model import MyScreenModel,Modif
from view import View
from kivy.uix.widget import Widget

class Modif(Widget):
    # Réinitialise le champ Textinput
    def reinit(self):

        self.ids.input.text = ""
    # Revient à l'action précédente
    def retour(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression

    # function take button inputs pressed
    # by user
    def btnpressed(self, button):
        # expression to store all text field values
        expression = self.ids.input.text
        # if text field expression contains
        # error then set it to empty field
        if "Error" in expression:
            expression = ""
        # if text filed expression contains
        # 0 then first set the field to empty and
        # display the button text pressed by user
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"

    #Génère une erreur si incompatible avec le calcul

    def answer(self):
        expression = self.ids.input.text
        try:
            # evaluate text field expression
            # using eval() function
            self.ids.input.text = str(eval(expression))

        except:
            # set text field to Error if
            # try block throws an error
            self.ids.input.text = "Error"

class Controller:
    def __init__(self):
        self.model = MyScreenModel()
        self.vue = View(self)

    def main(self):
        self.vue.main()

if __name__ == '__main__':
    calculatrice = Controller()
    calculatrice.main()