import re

class Student:

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

    def setpostcode(self, postcode):
        if re.search(r"[1-9][0-9]{3}\s?[A-Z]{2}", postcode):
            self.__postcode = postcode
        else:
            print("Dit is geen postcode, hou het volgende format aan: 1000 HH")

    def getpostcode(self):
        return self.__postcode

    def setadres(self, straatnaam, huisnummer):
        if re.search("[A-Z][a-z]*", straatnaam):
            self.__straatnaam = straatnaam
        else:
            print("Dit is geen straatnaam")
        if re.search("[0-9]*[A-Z]?", huisnummer):
            self.__huisnummer = huisnummer
        else:
            print("Dit is geen huisnummer")

    def getadres(self):
        return " ".join([self.__straatnaam, self.__huisnummer])


def main():
    zacky = Student()
    zacky.setvoornaam("Zacky")
    print(zacky.getvoornaam())
    print(zacky.getpostcode())
    print(zacky.getadres())

main()