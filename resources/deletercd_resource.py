#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.deletercd_service import DeleteRcdService

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
        unit = args.get('unit','')

        d_rsp = self.deletercd_service.delete_unit(unit)
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg': "SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = {}
            
        return d_rsp, status_code 
    