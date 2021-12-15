class student:

    def __init__(self, voornaam, vooropleiding):
        self.__voornaam = voornaam
        self.__vooropleiding = vooropleiding

    def setvoornaam(self, voornaam):
        self.__voornaam = voornaam

    def getvoornaam(self):
        return self.__voornaam

    def setvooropleiding(self, vooropleiding):
        self.__vooropleiding = vooropleiding

    def getvooropleiding(self):
        return self.__vooropleiding


def main():
    hans = student("Hans", "MBO")
    print(hans.getvoornaam(), hans.getvooropleiding())

    # miguel = student()
    # miguel.setvoornaam("Miguel")
    # miguel.setvooropleiding("HAVO")
    # print(miguel.getvoornaam())
    #
    # gideon = student()
    # gideon.setvoornaam("Gideon")
    # print(gideon.getvoornaam())
    #
    # evy = student()
    # evy.setvoornaam("Evy")
    # print(evy.getvoornaam())


main()