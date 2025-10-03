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

        if d_rsp.get('rsp','ERR') == 'OK':
            pkconfig = d_rsp.get('pkconfig',None)
            try:
                d_config = pickle.loads(pkconfig)
                return {'rsp':'OK', 'd_config': d_config }
            except Exception as e:
                return {'rsp':'ERR'}
            
        else:
            return {'rsp':'ERR'}
        
    def update_config(self, unit=None, d_params=None):
        """
        Recibe un dict pero envia al repositorio un pickle
        """
        self.logger.debug("")

        try:
            pkconfig = pickle.dumps(d_params)
        except Exception as e:
            return {'rsp':'ERR', 'msg':e }

        d_rsp =  self.repo.update_config(unit, pkconfig)
    
        return d_rsp
        


                