class Bureau():
    BUREAUX = []

    def __init__(self, **attributes):
        [setattr(self,k,v) for k,v in attributes.items()]

    def changeAttr(self,attr: str,value):

        self.__setattr__(attr,value)

    @classmethod
    def AchatBureau(cls, employe):
        bureau = Bureau(**{"prix": random.radrange(400,800), "salarie": employe})
        if employe is not None:
            employe.bureau = bureau
        cls.BUREAUX.append(bureau)

   # def venteBureau(cls,employe):