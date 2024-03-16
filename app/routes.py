from .resources import TransportePublico

def initialize_routes(api):
    api.add_resource(TransportePublico, '/transporte', '/transporte/<int:id>')
