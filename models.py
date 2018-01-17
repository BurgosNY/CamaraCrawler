from pendulum import parse, now
from mongoengine import Document, IntField, DateTimeField, StringField,\
 DictField, URLField, connect


# conecta a uma instância local do MongoDB, no database 'CamaraFederal'.
# Os documentos irão para essa DB, na coleção "lei"
connect(db='CamaraFederal')


class Lei(Document):
    leiId = IntField(required=True, unique=True)
    numero = IntField()
    ano = IntField()
    dataApresentacao = DateTimeField()
    ementa = StringField()
    statusProposicao = DictField()
    urlInteiroTeor = URLField()
    uriAutores = StringField()
    tipoAutor = StringField()
    siglaTipo = StringField()
    atualizado = DateTimeField(default=now())
    texto = StringField()
