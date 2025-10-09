#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

class DebugIdService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def read_debugid(self):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.read_debugid()
        # Como la respuesta es un bytestring lo debo convertir
        if d_rsp.get('status_code',0) == 200:
            debugid = d_rsp.get('debugid',b'').decode()
            d_rsp = {'status_code':200, 'debugid': debugid }

        return d_rsp
    
    def set_debugid(self, debugid=None):
        """
        """
        self.logger.debug("")
        d_rsp =  self.repo.set_debugid(debugid)
        if d_rsp.get('status_code',0) == 200:
            d_rsp = {'status_code':200, 'debugid': debugid }

        return d_rsp
        

