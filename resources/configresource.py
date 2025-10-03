#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
import pickle
from container import Container
from servicios.configservice import ConfigService


class ConfigResource(Resource):

    @inject
    def __init__(self, service: ConfigService = Provide[Container.config_service], logger = Provide[Container.logger]):
        self.config_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve la configuracion del dispositivo en un json.
        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args['unit']

        d_rsp = self.config_service.read_config(unit)

        return d_rsp, 200
 
    def put(self):
        ''' 
        Actualiza(override) la configuracion para la unidad
        NO CHEQUEA EL FORMATO
        '''
        #
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args['unit']
        d_params = request.get_json()
    
        d_rsp = self.config_service.update_config(unit, d_params)
     
        return {'rsp':'OK'}, 200         

