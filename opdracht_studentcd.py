import re


class student:

    def setvoornaam(self, voornaam):
        if re.search("[A-Z][a-z]*", voornaam):
            self.__voornaam = voornaam
        else:
            print("Dit is geen voornaam")

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
    daria = student()
    daria.setvoornaam("Daria")
    daria.setachternaam("Gajewska")
    print(daria.getachternaam())
    exit()
    print(daria.getvoornaam())

    luca = student()
    luca.setvoornaam("luca")
    print(luca.getvoornaam())

main()