#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import pickle

class ConfigService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def read_config(self, unit=None):
        """
        """
        self.logger.debug("")

        d_rsp = self.repo.read_config(unit)

        if d_rsp.get('status_code',0) == 200:
            # pkconfig es un string
            pkconfig = d_rsp.get('pkconfig', '')
            try:
                d_config = pickle.loads(pkconfig)
                assert isinstance(d_config, dict)

                d_rsp = {'status_code':200, 'd_config': d_config }
                
            except Exception as e:
                self.logger.error( f"ConfigService:read_config: {e}")
                d_rsp = {'status_code':502, 'msg':f"{e}"}

        return d_rsp
        
    def update_config(self, unit=None, d_params=None):
        """
        Recibe un dict pero envia al repositorio un pickle
        """
        self.logger.debug("")

        try:
            pkconfig = pickle.dumps(d_params)
        except Exception as e:
            self.logger.error( f"ConfigService:update_config: {e}")
            d_rsp = {'status_code':502, 'msg':f"{e}"}
            return d_rsp

        d_rsp = self.repo.update_config(unit, pkconfig)

        return d_rsp
    
    
        


                