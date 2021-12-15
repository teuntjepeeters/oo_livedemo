class fasta:

    def __init__(self, header):
        self.__header = header
        self.__sequenties = []

    def setheader(self, header):
        if header.startswith(">"):
            self.__header = header
        else:
            print("header is geen header")

    def getheader(self):
        return self.__header

    def setsequentie(self, seq):
        self.__sequenties.append(seq)

    def getsequentie(self):
        return "".join(self.__sequenties)


def main():
    f = fasta(">Sequentie1")
    #f.setheader(">Sequentie1")
    f.setsequentie("ATGGGTCAATGACCTAG")
    print(f.getsequentie())
    f.setsequentie("GGGAAATTCCCCCCCCCCCCCCCCCCCCCC")
    print(f.getsequentie())

    # Underscores
    print(int(4))
    int_ = 5
    print(int_)


main()