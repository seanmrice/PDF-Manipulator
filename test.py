from PyPDF2 import PdfFileReader,PdfFileWriter
import os

file = "file.pdf"
input = PdfFileReader(file)
output = PdfFileWriter()
input.getPage(0).mergeTranslatedPage(page2=input.getPage(1),tx='0',ty='-384')
output.addPage(input.getPage(0))
outputStream = file('fileout.pdf','wb')
output.write(outputStream)