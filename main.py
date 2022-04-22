import PyPDF2


def pdfInfo(inputFile):
    pdf = PyPDF2.PdfFileReader(inputFile, strict=False)
    pages_no = pdf.numPages
    current_page = pdf.getPage(0)
    pdf_media_box = current_page.mediaBox
    current_pdf_width = pdf_media_box[2]
    current_pdf_height = pdf_media_box[3]
    return [pages_no, current_pdf_height, current_pdf_width]


def TwoLTR2Tab(input_file, output_file):
    # Convert 2 PDF Pages to 1 11x17 page
    page_count = PyPDF2.PdfFileReader.getNumPages(input_file)
    pdf_info = pdfInfo(input_file)
    orientation = OrientationCheck(pdf_info[2], pdf_info[1])
    if page_count > 2:
        return print("PDF file must only be 2 pages")
    else:
        if orientation == "portrait":
            with open(input_file, "rb+"):
                read_pdf = PyPDF2.PdfFileReader(input_file)
                # TODO Continue buildout of PDF combination
        else:
            return print("PDF is not set up correctly")


# OrientationCheck returns the orientation of the PDF page (portrait, landscape, or square) as a string
def OrientationCheck(currentPdfWidth, currentPdfHeight):
    if currentPdfWidth > currentPdfHeight:
        return "landscape"
    if currentPdfWidth < currentPdfHeight:
        return "portrait"
    if currentPdfWidth == currentPdfHeight:
        return "square"


def SizeCheck(currentPdfWidth, currentPdfHeight, newHeight, newWidth):
    if currentPdfWidth == newWidth and currentPdfHeight == newHeight:
        print("PDF does not need resizing")
        return "false"
    return "true"


def main():
    print("Placeholder")


if __name__ == '__main__':
    main()
