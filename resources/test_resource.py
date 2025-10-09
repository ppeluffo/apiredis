#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource
from flask import request
from dependency_injector.wiring import inject, Provide
from container import Container

class TestResource(Resource):

    @inject
    def __init__(self, logger = Provide[Container.logger]):
        self.logger = logger

    def get(self):
        """
        """
        self.logger.debug("")

        data = {'KIYU001': [('HTQ1', 'ALTURA_TANQUE_KIYU_1'), ('HTQ2', 'ALTURA_TANQUE_KIYU_2')],
                 'SJOSE001': [('PA', 'PRESION_ALTA_SJ1'), ('PB', 'PRESION_BAJA_SQ1')],
                 'VALOR1':1.23,
                 'VALOR2':-34.5}

        return {'data': data }, 200
    
    def put(self):
        """
        """
        self.logger.debug("")
        
        d_params = request.get_json()
        self.logger.debug(f"d_params={d_params}")

        td = type(d_params)
        self.logger.debug(f"td={td}")
 
        return {'test':'put_test'}, 200