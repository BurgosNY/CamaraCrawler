# Câmara Crawler

## Dependências do Sistema

Para converter os arquivos da Câmara (PDF, DOCX etc.) você precisará instalar
softwares que não são feitos em Python. Para isso, siga as instruções do
[textract](http://textract.readthedocs.io/en/stable/installation.html).

Depois, instale o MongoDB. O jeito mais fácil é via homebrew
(`brew install mongo`), caso você esteja no Mac OS X. Se optar por fazer de
outra forma, [siga a
documentação](https://docs.mongodb.com/manual/installation/). Inicie uma
instância local na sua máquina via brew ou pelo comando `mongod`.

## Dependências Python

Depois, instale as dependências Python:

```bash
pip install -r requirements.txt
```

Caso vá desenvolver, instale as dependências de desenvolvimento para rodar os
testes, verificar estilo de código etc:

```bash
pip install -r requirements-dev.txt
```

## Rodando

Execute o comando:

```bash
python camara_api_crawler.py
```

No prompt, digitar o ano para baixar as leis, e esperar ele fazer o serviço.


## Visualizando o Banco de Dados

Opcional: instale o [Robo 3T](https://robomongo.org/), para ter uma
visualização das leis.

## Style Guide

Para verificar se seu código está seguindo as convenções de estilo criadas na
[PEP-8](https://www.python.org/dev/peps/pep-0008/), rode o comando:

```bash
pycodestyle *.py
```
