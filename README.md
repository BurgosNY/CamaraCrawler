## Câmara Crawler

Antes de instalar, siga as instruções do [textract](http://textract.readthedocs.io/en/stable/installation.html), responsável por fazer o parse de documentos .pdf. Ele tem uma série de dependências. Siga as instruções na página.

Depois, instale o MongoDB. O jeito mais fácil é via homebrew (`brew install mongo`). Se optar por fazer de outra forma, [siga a documentação](https://docs.mongodb.com/manual/installation/). Inicie uma instância local na sua máquina via brew ou pelo comando `mongod`.

Depois, instale as outras bibliotecas:

`pip install requirements.txt`

Opcional: instale o [Robo 3T](https://robomongo.org/), para ter uma visualização das leis. 

Depois é só rodar:
`python camara_api_crawler.py`

No prompt, digitar o ano para baixar as leis, e esperar ele fazer o serviço.
