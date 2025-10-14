#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import logging
from utilidades.login_config import set_log_level

class LogLevelService:
    """
    """
    def __init__(self, logger):
        self.logger = logger
    
    def set_log_level(self, level=None, timeout=60):
        """
        """
        self.logger.debug("")

        try:
            _ = set_log_level(level, timeout)
            d_rsp = {'status_code':200 }
            
        except ValueError as e:
            d_rsp =  {'status_code': 400, "msg": str(e)}
        
        return d_rsp

    def get_log_level(self):
        """
        Devuelve el nivel de log actual (global o por equipo).
        """
        logger = logging.getLogger('app')
        current_level = logging.getLevelName(logger.getEffectiveLevel())
        d_rsp = {'status_code':200, "logger": "app", "current_level": current_level}
        
        return d_rsp