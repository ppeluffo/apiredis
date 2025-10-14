#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
import pickle
from container import Container
from servicios.queue_service import QueueService

class RxDataQueueLengthResource(Resource):

    @inject
    def __init__(self, service: QueueService = Provide[Container.queue_service], logger = Provide[Container.logger]):
        self.queue_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve la cantidad de elementos en la cola
        """
        self.logger.debug("")

        d_rsp = self.queue_service.get_length("RXDATA_QUEUE")
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
    
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 200:
            qlength = d_rsp.get('length',0) 
            d_rsp = {'length': qlength }
        elif status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = { }
    
        return d_rsp, status_code 
    
 