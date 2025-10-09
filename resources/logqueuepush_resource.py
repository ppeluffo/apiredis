#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
import json
from container import Container
from servicios.queue_service import QueueService

class LogQueuePushResource(Resource):

    @inject
    def __init__(self, service: QueueService = Provide[Container.queue_service], logger = Provide[Container.logger]):
        self.queue_service = service
        self.logger = logger
 
    def put(self):
        ''' Recibe un string que lo serializa y almacena en la cola

            data = "TAG=CPN7Z9N8J LB=START TS=2025-04-29 08:47:34.414475 ID=DNOTQ001 TYPE=SPQ_AVRDA VER=1.1.0 HW=None CLASS=PING"
            j_data = json.dumps(data)
            req=requests.put('http://127.0.0.1:5100/apiredis/dataline', json=j_data)
            json.loads(req.json())

        '''
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('log_data',type=str,location='json',required=True)
        args=parser.parse_args()
        payload = args.get('log_data', None)
        assert isinstance(payload, str)

        d_rsp = self.queue_service.rpush("LOG_QUEUE", payload)
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            _ = d_rsp.pop('msg', '')
            d_rsp['msg'] = "SERVICIO NO DISPONIBLE TEMPORALMENTE"
        return d_rsp, status_code 

    
