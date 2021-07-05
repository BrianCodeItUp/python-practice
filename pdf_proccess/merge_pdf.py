import sys
import PyPDF2 as p

def pdf_combiner (pdf_list):
  merger = p.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(pdf)
  merger.write('super.pdf')
  print('file written successfully')

def main(pdf_list):
  pdf_combiner(pdf_list)

if (__name__ == '__main__'):
  inputs = sys.argv[1:]
  main(inputs)