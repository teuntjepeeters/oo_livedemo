class fasta:

    def setheader(self, header):
        if header.startswith(">"):
            self.__header = header
        else:
            print("header is geen header")

    def getheader(self):
        return self.__header

    def setsequentie(self, seq):
        self.__seq = seq

    def getsequentie(self):
        return self.__seq


def main():
    f = fasta()
    f.setheader(">Sequentie1")
    f.__header = "Ja hoi"
    print(f.getheader())
    f.setheader(">Ja hoi")
    print(f.getheader())
    f.setsequentie("ATGGGTCAATGACCTAG")
    f.__seq = "GGAT"
    print(f.getsequentie())

main()