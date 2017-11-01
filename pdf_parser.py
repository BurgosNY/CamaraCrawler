import os
from bs4 import BeautifulSoup


class PdfToString:
    '''Transforms a PDF file into a string. Can use a remote (URL)
    or local file location. There's an option to save the file.
    Set a timeout for when to stop retrieving the data.
    '''
    # TO DO: Implement better timeout method, use "yeld"

    def __init__(self, location, save=False, filename="pdf_file.pdf"):
        self.location = location
        self.save = save
        self.filename = filename

    def download(self):
        ''' Use only if the file is located on the web:
        '''
        import urllib
        try:
            # TO DO: Find a way to have the type specified in the request (
            # .doc or .pdf)
            urllib.request.urlretrieve(self.location, self.filename)
            print(f'file saved as {self.filename}')
        except urllib.error.ContentTooShortError:
            raise UrlError('Download error. Check the url or the connection.')

    def convert(self):
        ''' Downloads a PDF file, parse it with BeautifulSoup and transform
        it to a String. Uses textract: http://textract.readthedocs.io/en/stable/
        '''
        import textract
        source_file = self.download()
        try:
            source_binary = textract.process(self.filename, encoding='utf_8',
                                             method='pdftotext', layout=True)
            soup = BeautifulSoup(source_binary, "html.parser")
            text_string = soup.prettify(formatter=None)
        except textract.exceptions.ShellError:
            # TO DO: Implement a way to handle non-pdf files
            print('Not a pdf')
            raise NameError('The file is not a .pdf')


        # Deletes the file if not explicitly set to save
        if not self.save:
            os.remove(self.filename)
        return text_string
