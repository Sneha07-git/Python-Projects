import PyPDF2
import sys

inputs = sys.argv[1:]

def combine_pdf(pdf_list):
	merger = PyPDF2.PdfFileMerger()

	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

combine_pdf(inputs)


'''
with open('dummy.pdf','rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
'''