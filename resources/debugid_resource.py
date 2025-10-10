#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.debugid_service import DebugIdService

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
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code 
        

    def put(self):
        ''' 
        Actualiza el DEBUG_ID
        Como es PUT, la orden la mandamos en un json
        '''
        self.logger.debug("")
        #
        parser = reqparse.RequestParser()
        parser.add_argument('debugid', type=str ,location='json',required=True)
        args=parser.parse_args()
        debugid = args.get('debugid','DEFAULT')

        assert isinstance(debugid, str)

        d_rsp = self.debugid_service.set_debugid(debugid)
        
        assert isinstance(d_rsp, dict)

        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code 
    
