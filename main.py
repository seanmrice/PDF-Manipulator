import os
import re
from docx2pdf import convert
import PyPDF2


def convert_d2p(folder_in, folder_out):
    try:
        convert(folder_in, folder_out)
    except NameError:
        return print("Error: ", NameError)
    finally:
        return True


folder_to_convert = os.listdir("/Users/sean/Convert")
folder_to_output_to = ("/Users/sean/Convert")
for item in folder_to_convert:
    if re.search(".docx", item):
        print(item)
        convert_d2p(item, folder_to_output_to)
