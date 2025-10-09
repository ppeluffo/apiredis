#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
import pickle
from container import Container
from servicios.queue_service import QueueService

class DequeueRxLinesResource(Resource):

    @inject
    def __init__(self, service: QueueService = Provide[Container.queue_service], logger = Provide[Container.logger]):
        self.queue_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve la cantidad count de elementos datalines encolados .
        """
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('count',type=str,location='args',required=True)
        args=parser.parse_args()
        count = args['count']

        d_rsp = self.queue_service.dequeue_rxlines(count)
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code 
    
 
 