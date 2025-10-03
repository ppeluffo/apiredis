#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.ordenesservice import OrdenesService

class OrdenesResource(Resource):

    @inject
    def __init__(self, service: OrdenesService = Provide[Container.ordenes_service], logger = Provide[Container.logger]):
        self.ordenes_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve las ordenes para la unidad en un json
            Invocacion: /apiredis/ordenes?unit=DLGID

            Testing:
            req=requests.get('http://127.0.0.1:5100/apiredis/ordenes',params={'unit':'DLGTEST'})
            json.loads(req.json())
            {'ordenes': 'RESET;PRENDER_BOMBA'}

        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args['unit']

        d_rsp = self.ordenes_service.get_ordenes(unit)
        
        return d_rsp, 200
   
    def put(self):
        """
          Actualiza(override) las ordenes para la unidad
            NO CHEQUEA EL FORMATO DE LA LINEA DE ORDENES
            Invocacion: /apiredis/ordenes?unit=DLGID
            Como es PUT, la orden la mandamos en un json {'ordenes':orden }

            Testing:
            d={'ordenes':'Reset;Apagar;Prender'}
            jd=json.dumps(d)
            req=requests.put('http://127.0.0.1:5100/apiredis/ordenes', params={'unit':'DLGTEST'}, json=jd)
            json.loads(req.json())

        """
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        parser.add_argument('ordenes',type=str,location='json',required=True)
        args=parser.parse_args()
        unit = args['unit']
        ordenes = args['ordenes']
        #
        d_rsp = self.ordenes_service.set_ordenes(unit, ordenes)
        
        return d_rsp, 200
    