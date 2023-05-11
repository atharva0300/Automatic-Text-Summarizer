import re
import PyPDF2

file = open('steeringwheel.pdf','rb')
reader = PyPDF2.PdfReader(file)
page1 = reader.pages[0]
print("The Size of the Documents is",len(reader.pages),"pages.")
pdfData= page1.extract_text()

# Define a regular expression pattern to match abbreviations
pattern = r'\b([A-Z]{2,})\b'

# Find all abbreviations in the document
abbreviations = re.findall(pattern, pdfData)

# Print the abbreviations
print("Abbreviations found are as follows:")
for abbr in abbreviations:
    print(abbr)

