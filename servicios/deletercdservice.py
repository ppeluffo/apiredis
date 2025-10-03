#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

class DeleteRcdService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def delete_unit(self,unit=None):
        """
        """
        self.logger.debug("")
        return self.repo.delete_unit(unit)