class fasta:

    def setheader(self, header):
        if ">" in header:
            self.__header = header
        else:
            print("Dit is geen header")

    def getheader(self):
        return self.__header

    def setsequentie(self, sequentie):
        self.__sequentie = sequentie

    def getsequentie(self):
        return self.__sequentie


def main():
    # f1 = fasta()
    # f1.setheader(">Sequentie")
    # print(f1.getheader())
    # f1.__header = "Joehoe"
    # print(f1.getheader())
    # f1.setheader(">Joehoe")
    # print(f1.getheader())
    #
    print("Hello world! ")
    print_ = "Hello world!"
    print(print_)


main()