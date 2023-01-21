from PyPDF2 import PdfReader, PageObject
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You must enter file root!')
        sys.exit()

    root : str = sys.argv[1]
    try:
        reader : PdfReader = PdfReader(root)
        pages : list[PageObject] = reader.pages
        with open('output.txt', 'w') as file:
            page : PageObject
            for index, page in enumerate(pages):
                print(f'Reading page {index + 1}')
                file.write(f'----------{index + 1}----------\n\n\n')
                file.write(page.extract_text())
                file.write('\n\n\n')
            print('File is ready')
    except FileNotFoundError:
        print('File not found. Check the root')
        sys.exit()

    except UnicodeEncodeError:
        print('Error: file cannot be read.')
        sys.exit()
