class student:

    def setvoornaam(self, voornaam):
        self.__voornaam = voornaam

    def getvoornaam(self):
        return self.__voornaam

    def setvooropleiding(self, vooropleiding):
        self.__vooropleiding = vooropleiding

    def getvooropleiding(self):
        return self.__vooropleiding


def main():
    hans = student()
    hans.setvoornaam("Hans")
    hans.setvooropleiding("MBO")
    print(hans.getvoornaam(), "vooropleiding:", hans.getvooropleiding())

    miguel = student()
    miguel.setvoornaam("Miguel")
    miguel.setvooropleiding("HAVO")
    print(miguel.getvoornaam(), "vooropleiding:", miguel.getvooropleiding())


main()