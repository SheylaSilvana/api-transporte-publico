from .models import Transporte

def carregar_dados_transporte(origem=None, destino=None):
    query = Transporte.query
    if origem:
        query = query.filter(Transporte.origem.like(f"%{origem}%"))
    if destino:
        query = query.filter(Transporte.destino.like(f"%{destino}%"))
    return [d.to_dict() for d in query.all()]