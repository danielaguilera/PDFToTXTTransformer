from PyPDF2 import PdfReader, PageObject
import sys

PARAMS_PATH = 'Params.txt'

def isPDFFile(filename : str):
    return filename.endswith('.pdf')

if __name__ == '__main__':

    # roots : list[str] = list(filter(lambda filename : isPDFFile(filename), os.listdir()))
    # if len(roots) > 0:
    #     print(f'{len(roots)} files found')
    # else:
    #     print('No PDF files found')
    #     sys.exit()
    # root : str

    try:
        with open(PARAMS_PATH, 'r') as file:
            root : str = rf"{file.readline()}"
    except FileNotFoundError:
        print('Params file missing')
        sys.exit()

    try:
        reader : PdfReader = PdfReader(root)
        pages : list[PageObject] = reader.pages
        with open(root.replace('.pdf', '.txt'), 'w') as file:
            page : PageObject
            print(f'Converting {root}')
            for index, page in enumerate(pages):
                print(f'Reading page {index + 1}')
                file.write(page.extract_text())
                file.write('\n\n')
            print('File is ready')
    except UnicodeEncodeError:
        print('Error: file cannot be read.')
