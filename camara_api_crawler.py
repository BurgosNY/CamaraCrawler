from urllib.request import urlopen, Request
import ssl
import json
from pendulum import parse
from models import Lei


# Dependendo da instalação do Python, é necessário este certificado:
certificate = ssl._create_unverified_context()


def leis_recentes(ano_apresentacao):
    '''
    Usa a API de dados abertos da Câmara para ver as leis apresentadas
    recentemente. Quando a API for melhorada
    (issue: https://github.com/labhackercd/dados-abertos/issues/102)
    será possível pegar só os dados mais recentes.
    '''
    leis_ids = []
    # link da primeira página
    camara_request = f'https://dadosabertos.camara.leg.br/api/v2/proposicoes?ano={ano_apresentacao}&pagina=1&itens=100'
    # add cabeçalho para api retornar json
    req = Request(camara_request)
    req.add_header('accept','application/json')
    
    list_end = True

    while list_end:        
        r = urlopen(req, context=certificate)
        leis = json.loads(r.read())
        # yield lei id
        for lei in leis['dados']:
            yield lei['id']
        # verifica se última página
        if 'next' not in [x['rel'] for x in leis['links']]:
            list_end =False
            continue
        # captura o link da próxima página 
        next_page = next(x for x in leis['links'] if x['rel'] == 'next')
        camara_request = next_page['href']
        req = Request(camara_request)
        req.add_header('accept','application/json')


def upload_leis(lista_de_leisIDs):
    '''
    Usando o Schema do Models e a API dos dados abertos para padronizar
    os projetos de lei e subir todos em um banco de dados
    '''
    # TO DO: ver se é necessário fazer connect(db='CamaraFederal')
    for prop in lista_de_leisIDs:
        req = Request(f'https://dadosabertos.camara.leg.br/api/v2/proposicoes/{prop}')
        req.add_header('accept','application/json')
        r = urlopen(req, context=certificate).read()
        prop_j = json.loads(r)
        #print(prop_j)
        data = prop_j['dados']
        print(data)
        novaLei = Lei(
            leiId=prop,
            numero=data['numero'],
            ano=data['ano'],
            ementa=data['ementa'],
            dataApresentacao=parse(data['dataApresentacao'],
                                   tz='America/Sao_Paulo'),
            statusProposicao=data['statusProposicao'],
            urlInteiroTeor=data['urlInteiroTeor'],
            uriAutores=data['uriAutores'],
            tipoAutor=data['tipoAutor'],
            siglaTipo=data['siglaTipo']
            # TO DO: Ver se é necessário passar o "atualizado"
        )
        novaLei.save()


def leis_to_string():
    '''
    AVISO: Essa função leva .4 segundos por lei. Pode demorar bastante
    se estiver baixando várias. Apenas tualiza leis sem texto.
    TO DO: Usar async // Usar aiohttp Library
    '''
    for lei in Lei.objects(texto__exists=0):
        try:
            txt_lei = PdfToString(lei.urlInteiroTeor).convert()
            lei.save(texto=txt_lei)
        except NameError:
            continue


if __name__ == '__main__':
    ano_busca = input('Para qual ano você deseja buscar as leis? Ex: 2017 \n> ')
    leis_para_parsear = leis_recentes(ano_busca)
    upload_leis(leis_para_parsear)
    leis_to_string()
