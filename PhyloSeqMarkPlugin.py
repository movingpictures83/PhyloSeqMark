import PyPluMA

class PhyloSeqMarkPlugin:
    def input(self, filename):
        self.parameters = dict()

        infile = open(filename, 'r')
        for line in infile:
            contents = line.strip().split('\t')
            self.parameters[contents[0]] = contents[1]

        otufile = open(PyPluMA.prefix()+"/"+self.parameters["otu"], 'r')
        taxfile = open(PyPluMA.prefix()+"/"+self.parameters["tax"], 'r')
        self.mark = self.parameters["mark"]

        self.otulines = []
        self.taxlines = []

        self.otuheader = otufile.readline()
        for line in otufile:
            self.otulines.append(line)

        for line in taxfile:
            self.taxlines.append(line)


    def run(self):
        self.headercontents = self.otuheader.split(',')
        for i in range(1, len(self.headercontents)):
            self.headercontents[i] = '\"' + self.mark + self.headercontents[i][1:]
        for i in range(0, len(self.otulines)):
            self.otulines[i] = '\"' + self.mark + self.otulines[i][1:]
        for i in range(1, len(self.taxlines)):
            self.taxlines[i] = '\"' + self.mark + self.taxlines[i][1:]

    def output(self, filename):
        outotufile = open(filename+".otu.csv", 'w')
        outtaxfile = open(filename+".tax.csv", 'w')

        for i in range(len(self.headercontents)):
            outotufile.write(self.headercontents[i])
            if (i != len(self.headercontents)-1):
                outotufile.write(',')
            #else:
            #    outotufile.write('\n')

        for line in self.otulines:
            outotufile.write(line)

        for line in self.taxlines:
            outtaxfile.write(line)
