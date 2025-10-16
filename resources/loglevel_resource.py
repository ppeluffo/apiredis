#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse, request
from dependency_injector.wiring import inject, Provide
from utilidades.tolerant_json_load import tolerant_json_load
from container import Container
from servicios.loglevel_service import LogLevelService

class LogLevelResource(Resource):

    @inject
    def __init__(self, service: LogLevelService = Provide[Container.loglevel_service], logger = Provide[Container.logger]):
        self.loglevel_service = service
        self.logger = logger

    def post(self):
        """
        Permite cambiar el nivel de log de un equipo, con timeout opcional.
        POST /api/loglevel
        Body: {"equipo": "UYRIV114", "level": "DEBUG", "timeout": 600}
        """
        self.logger.debug("")

        #data = request.get_json(force=True)
        # Safe json loads
        try:
            raw_body = request.data.decode("utf-8")
            if not raw_body:
                return {},400 
            d_params, reparado = tolerant_json_load(raw_body)

        except Exception as e:
            self.logger.error( f"{e}")
            return {}, 400

        if reparado:
            self.logger.info(f"d_params Reparado JSON !!")    
        self.logger.debug(f"d_params={d_params}")
       
        level = d_params.get("level")
        timeout = d_params.get("timeout", None)

        assert isinstance(level, str)
        assert isinstance(timeout, int)
        
        d_rsp = self.loglevel_service.set_log_level(level, timeout)

        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        
        assert isinstance(d_rsp, dict)
        return d_rsp, status_code
    
    def get(self):
        """
        Devuelve el nivel de log actual (global o por equipo).
        """
        d_rsp = self.loglevel_service.get_log_level()

        status_code = d_rsp.pop('status_code', 500)
        
        # No mando detalles de los errores en respuestas x seguridad. 
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        
        assert isinstance(d_rsp, dict)
        return d_rsp, status_code
        
