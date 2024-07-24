import PyPDF2

#update the name of your pdf files below
pdfiles = ["file1 of your pdf.pdf","file2.pdf","file3.pdf"]

merger = PyPDF2.PdfMerger()
for name in pdfiles:
    file = open(name,'rb')
    pdfReader = PyPDF2.PdfReader(file)
    merger.append(pdfReader)
file.close()
merger.write("name of your pdf here.pdf")