class MarkdownWriter:

    def __init__(self):
        self.bold = False
        self.italic = False
        self.code = False
        self.autospacing = True


    def openFile(self, fileName):
        self.file = open(fileName, 'w')

    def writeTitle(self, title, size):
        title = self.styleWords(title)
        for i in range(size):
            self.file.write('#')
        self.file.write(title)
        self.spacing()

    def insertImage(self, imagePath):
        self.file.write("![alt text](")
        self.file.write(imagePath + ")")
        self.spacing()


    def writeText(self, text):
        text = self.styleWords(text)
        self.file.write(text)
        self.spacing()

    def insertLink(self, text, URL):
        self.file.write("[" + text + "](" + URL +")")
        self.spacing()

    def closeFile(self):
        self.file.close()

    def setBold(self, value):
        if value == True:
            self.bold = True
        else:
            self.bold = False

    def setItalic(self, value):
        if value == True:
            self.italic = True
        else:
            self.italic = False

    def setCode(self, value):
        if value == True:
            self.code = True
        else:
            self.code = False

    def styleWords(self, text):
        if self.code == True:
            text = "`" + text + "`"
        if self.bold == True:
            text = "**" + text + "**"
        if self.italic == True:
            text = "_" + text + "_"

        return text

    def setAutospacing(self, value):
        self.autospacing = value

    def insertSpace(self, number = 1):
        for i in range(number):
            self.file.write("\n")

    def spacing(self):
        if self.autospacing == True:
            self.file.write("\n")

    def insertMatrix(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        self.file.write("||")
        for i in range(rows):
            self.file.write(str(i) + "|")
        self.file.write("\n")
        self.file.write("|---|")
        for i in range(rows):
            self.file.write("--- |")
        self.file.write("\n")
        for i in range(rows):
            self.file.write("|**" + str(i) + "**|")
            for j in range(columns):
                self.file.write( str(matrix[i][j]) + "|")
            self.file.write("\n")


def main():
    pass

if __name__ == '__main__':
    main()
