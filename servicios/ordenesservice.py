#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import pickle


class OrdenesService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_ordenes(self, unit):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.get_ordenes(unit)
    
        if d_rsp.get('rsp','ERR') == 'OK':
            pk_ordenes = d_rsp['pk_ordenes']
            if pk_ordenes is None:
                ordenes = None
            else:
                try:
                    ordenes = pickle.loads(pk_ordenes) 
                except Exception:
                    return {'rsp':'ERR', 'msg': 'pickle loads error'}
            d_rsp = {'rsp':'OK', 'ordenes':ordenes}
            return d_rsp
    
    def set_ordenes(self, unit=None, ordenes=None):
        """
        """
        self.logger.debug("")

        try:
            pk_ordenes = pickle.dumps(ordenes)
        except Exception:
            d_rsp = {'rsp':'ERR', 'msg':'pickle dumps error'}
            return d_rsp
        #
        return self.repo.set_ordenes(unit, pk_ordenes)
        

