# Import modules
import pyttsx3
import PyPDF2

# select the files
# in place of example.pdf state the pdf name
book = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

# loop for reading the whole book
# in place of select page type the page number of the pdf
startpage = 1
for num in range(startpage, pages):
    page = pdfReader.getPage(4)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# Install: 
# pip install wheel
# pip install pyttsx3
# pip install PyPDF2 
# in terminal 