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
        d_rsp = self.repo.delete_unit(unit)
        if d_rsp.get('status_code',0) == 200:
            d_rsp = {'status_code': 200, 'unit': unit}
    
        return d_rsp
    