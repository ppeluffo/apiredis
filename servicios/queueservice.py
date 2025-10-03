#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import pickle

class QueueService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_length(self, qname=None):
        """
        """
        self.logger.debug("")
        return self.repo.get_length(qname)
         
    def pop(self, qname=None, count=None):
        """
        Los datos de la cola no estan pickleados pero si son binary.
        Hay que decodificarlos
        """
        self.logger.debug("")
        
        d_rsp = self.repo.pop(qname, count)
        if d_rsp.get('rsp','ERR') == "OK":
            l_datos = d_rsp['l_datos']
            l_datos = [ x.decode() for x in l_datos ]
            d_rsp = {'rsp':'OK', 'l_datos': l_datos}

        return d_rsp
    
    def pop_and_unpickle(self, qname=None, count=None):
        """
        Asumimos que los datos de la cola estan pickleados
        """
        self.logger.debug("")

        d_rsp = self.repo.pop(qname, count)
        
        #self.logger.debug(f"d_rsp={d_rsp}")

        if d_rsp.get('rsp','ERR') == 'OK':
            l_pkdatos = d_rsp['l_datos']
            if l_pkdatos is None:
                # app.logger.info( f'(024) ApiREDIS_ERR005: No l_pkdatos rcd')
                l_datos = []
            else:
            # Des-serializo los elementos de la lista.
                self.logger.debug(f"l_pkdatos={l_pkdatos}")
                l_datos = []
                for element in l_pkdatos:
                    try:
                        l_datos.append( pickle.loads(element))
                    except Exception:
                        return {'rsp':'ERR', 'msg':'pickle loads error'}
                
        #
        return { 'rsp':'OK', 'l_datos': l_datos}
       
    def push(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        return self.repo.push(qname, payload)


         
