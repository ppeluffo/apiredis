#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

class PingService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def ping(self):
        """
        """
        self.logger.debug("")
        return self.repo.ping()