from flask import request
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, Transporte

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

class TransportePublico(Resource):
    @auth.login_required
    def get(self):
        origem = request.args.get('origem')
        destino = request.args.get('destino')
        query = Transporte.query
        if origem:
            query = query.filter(Transporte.origem.like(f"%{origem}%"))
        if destino:
            query = query.filter(Transporte.destino.like(f"%{destino}%"))
        return {"dados": [d.to_dict() for d in query.all()]}, 200

    @auth.login_required
    def post(self):
        dados = request.get_json(force=True)
        novo_transporte = Transporte(**dados)
        db.session.add(novo_transporte)
        db.session.commit()
        return {"id": novo_transporte.id}, 201

    @auth.login_required
    def put(self, id):
        dados = request.get_json(force=True)
        transporte = Transporte.query.get_or_404(id)
        for chave, valor in dados.items():
            setattr(transporte, chave, valor)
        db.session.commit()
        return {"sucesso": "Dados atualizados com sucesso."}, 200

    @auth.login_required
    def delete(self, id):
        transporte = Transporte.query.get_or_404(id)
        db.session.delete(transporte)
        db.session.commit()
        return '', 204
