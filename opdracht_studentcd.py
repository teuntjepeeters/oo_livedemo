import re


class student:

    def __init__(self, voornaam, achternaam):
        self.setvoornaam(voornaam)
        # self.__voornaam = voornaam
        self.__achternaam = achternaam

    def setvoornaam(self, voornaam):
        if re.search("[A-Z][a-z]*", voornaam):
            self.__voornaam = voornaam
        else:
            print("Dit is geen voornaam")
            self.__voornaam = ""

    def getvoornaam(self):
        return self.__voornaam

    def setachternaam(self, achternaam):
        if achternaam[0].upper() and achternaam[1:].lower():
            self.__achternaam = achternaam
        else:
            print("Dit is geen achternaam")

    def getachternaam(self):
        return self.__achternaam


def main():
    daria = student("daria", "Gajewska")
    print(daria.getvoornaam(), daria.getachternaam())

    glenn = student("Glenn", "Jepkes")
    print(glenn.getvoornaam(), glenn.getachternaam())
    exit()
    daria.setachternaam("Gajewska")
    print(daria.getachternaam())
    print(daria.getvoornaam())

    luca = student()
    luca.setvoornaam("luca")
    print(luca.getvoornaam())

    glenn = student()
    glenn.setvoornaam("Glenn")

    joshua = student()
    joshua.setvoornaam("Joshua")
    print(joshua.getvoornaam())
    print(joshua.__voornaam)

main()