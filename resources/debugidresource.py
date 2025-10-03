#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.debugidservice import DebugIdService

class DebugIdResource(Resource):

    @inject
    def __init__(self, service: DebugIdService = Provide[Container.debugid_service], logger = Provide[Container.logger]):
        self.debugid_service = service
        self.logger = logger

    def get(self):
        """
        Retorna el id de la unidad que debe hacerse el debug
        """
        self.logger.debug("")

        d_rsp = self.debugid_service.read_debugid()

        if d_rsp.get('rsp','ERR') == 'OK':
            # Como la respuesta es un bytestring lo debo convertir
            debugid = d_rsp.get('debugid',b'').decode()
            return {'rsp':'OK', 'debugid':debugid}, 200
        else:
            return d_rsp, 200
        
    def put(self):
        ''' 
        Actualiza el DEBUG_ID
        Como es PUT, la orden la mandamos en un json
        '''
        self.logger.debug("")
        #
        parser = reqparse.RequestParser()
        parser.add_argument('debugid',type=str,location='json',required=True)
        args=parser.parse_args()
        debugid = args['debugid']

        d_rsp = self.debugid_service.set_debugid(debugid)

        if d_rsp.get('rsp','ERR') == 'OK':
            return {'rsp':'OK'}, 200
        else:
            return d_rsp, 200
