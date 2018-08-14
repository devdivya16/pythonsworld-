import PyPDF2
pdfFileObject = open("C:\\Users\div\Desktop\Offer letter.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())