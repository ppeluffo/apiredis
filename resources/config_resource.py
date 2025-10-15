#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
from utilidades.parse_to_dict import parse_to_dict

from container import Container

from servicios.config_service import ConfigService


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
        assert isinstance(d_rsp, dict)

        status_code = d_rsp.pop('status_code', 500)
        d_config = d_rsp.pop('d_config',{})

        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:  
            d_rsp = {'msg',"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = d_config

        return d_rsp, status_code
 
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
        d_p = request.get_json()
        
        d_params = parse_to_dict(d_p)
        assert isinstance(d_params, dict )
    
        d_rsp = self.config_service.update_config(unit, d_params)
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = {}
    
        return d_rsp, status_code      


