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
        return self.repo.read_debugid()
    
    def set_debugid(self, debugid=None):
        """
        """
        self.logger.debug("")
        return self.repo.set_debugid(debugid)
        

