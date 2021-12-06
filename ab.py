class fasta:

    def setheader(self, header):
        self.__header = header

    def getheader(self):
        return self.__header

    def setsequentie(self, seq):
        self.__seq = seq

    def getsequentie(self):
        return self.__seq


def main():
    f = fasta()
    f.setheader(">Sequentie1")
    print(f.getheader())
    f.setsequentie("ATGGGTCAATGACCTAG")
    print(f.getsequentie())
    # print(f)

main()