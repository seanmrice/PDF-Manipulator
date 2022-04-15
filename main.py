from pathlib import Path
from docx2pdf import convert


def convert_d2p(file_in):
    try:
        # file_out = open(file_out, "w")
        convert(file_in)
        # file_out.close()
    except NameError:
        return print("Error: ", NameError)
    finally:
        return True


folder_to_convert = "/Users/sean/Convert"
files_to_convert = list(Path(folder_to_convert).glob("*.docx"))
print(files_to_convert)
file_to_output_to = "/Users/sean/Convert/"

for item in files_to_convert:
    convert_d2p(item)
