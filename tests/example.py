from markdownWriter.markdownWriter  import MarkdownWriter
file = MarkdownWriter()

file.openFile("fileName.md")

file.setCode(True)
file.setBold(True)
file.setItalic(True)
file.writeTitle("This is the title.", 1)
file.setBold(False)
file.setCode(False)
file.setItalic(False)

file.writeTitle("This is the subtitle.", 2)

file.setItalic(True)
file.writeTitle("This is tinier subtitle.", 3)
file.setItalic(False)

file.writeText("This is a python library in Github.")
#file.insertImage("imagen.png")
file.insertSpace(2)

file.insertLink("Enlace a Github", "www.github.com")

file.insertSpace(2)
matrix = [[1,2,3,4],[1,1,2,1],[1,0,0,0]]
file.insertMatrix(matrix)


file.closeFile()
