import PyPDF2 as p

template = p.PdfFileReader(open('super.pdf','rb'))
watermark = p.PdfFileReader(open('wtr.pdf', 'rb'))
output = p.PdfFileWriter()

# iterate through each PDF list, merge PDF with watermark
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watered_output.pdf', 'wb') as file:
        output.write(file)
