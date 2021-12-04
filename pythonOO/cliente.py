class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #definindo o nome como objeto
    @property
    def nome(self):
        print("chamando o @property nome()")
        return self.__nome.title()

    # definindo o nome como setter
    @nome.setter
    def nome(self, nome):
        print("chamando o setter nome()")
        self.__nome = nome
