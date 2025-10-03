#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
import pickle
from container import Container
from servicios.queueservice import QueueService

class QueuePopResource(Resource):

    @inject
    def __init__(self, service: QueueService = Provide[Container.queue_service], logger = Provide[Container.logger]):
        self.queue_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve la cantidad count de elementos en la cola qname.
        Asumimos que la cola SI está pikleada.
        """
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('qname',type=str,location='args',required=True)
        parser.add_argument('count',type=str,location='args',required=True)
        args=parser.parse_args()
        qname = args['qname']
        count = args['count']

        d_rsp = self.queue_service.pop_and_unpickle(qname, count)

        return d_rsp, 200
 