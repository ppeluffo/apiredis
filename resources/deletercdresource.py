#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.deletercdservice import DeleteRcdService

class DeleteRcdResource(Resource):

    @inject
    def __init__(self, service: DeleteRcdService = Provide[Container.deletercd_service], logger = Provide[Container.logger]):
        self.deletercd_service = service
        self.logger = logger

    def delete(self):
        """
        """
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args['unit']

        d_rsp = self.deletercd_service.delete_unit(unit)

        if d_rsp.get('rsp','ERR') == 'OK':
            return {'rsp':'OK'}, 200
        else:
            return  {'rsp':'ERR'}, 200