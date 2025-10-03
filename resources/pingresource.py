#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.pingservice import PingService

class PingResource(Resource):

    @inject
    def __init__(self, service: PingService = Provide[Container.ping_service], logger = Provide[Container.logger]):
        self.ping_service = service
        self.logger = logger
        
    def get(self):
        # Solicito el servicio correspondiente.
        self.logger.debug("")
            
        d_rsp = self.ping_service.ping()

        if d_rsp.get('rsp','ERR') == 'OK':
            return d_rsp,200
        else:
            return d_rsp, 500

