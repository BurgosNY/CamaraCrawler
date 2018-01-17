import os
from bs4 import BeautifulSoup


class PdfToString:
    """Transforma um arquivo PDF em texto.

    Pode utilizar um endereço remoto (URL) ou um arquivo local.
    Existe uma opção para salvar o arquivo PDF localmente e para
    definir o tempo de espera até cancelar a busca.
    """
    # TODO: implementar um método melhor para timeout, usar 'yield'

    def __init__(self, location, save=False, filename="pdf_file.pdf"):
        self.location = location
        self.save = save
        self.filename = filename

    def download(self):
        """Executa o download, usada apenas se o conteudo estiver na Web."""

        import urllib
        try:
            # TODO: identificar uma maneira de definir o tipo na req (
            # .doc or .pdf)
            urllib.request.urlretrieve(self.location, self.filename)
            print(f'file saved as {self.filename}')
        except urllib.error.ContentTooShortError:
            raise UrlError('Download error. Check the url or the connection.')

    def convert(self):
        """Converte o PDF baixado anteriormente.

        Faz download de um arquivo PDF, executa o 'parser' do BeautifulSoup
        e transforma o mesmo em uma 'string' utilizando o textract:
        http://textract.readthedocs.io/en/stable/
        """

        import textract
        source_file = self.download()
        try:
            source_binary = textract.process(self.filename, encoding='utf_8',
                                             method='pdftotext', layout=True)
            soup = BeautifulSoup(source_binary, "html.parser")
            text_string = soup.prettify(formatter=None)
        except textract.exceptions.ShellError:
            # TODO: implementar uma maneira de lidar com arquivos nao PDF.
            print('Not a pdf')
            raise NameError('The file is not a .pdf')

        # Apaga o arquivo baixado caso não esteja explícito para salvar
        if not self.save:
            os.remove(self.filename)
        return text_string
