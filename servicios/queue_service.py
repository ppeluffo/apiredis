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
         
    def lpop(self, qname=None, count=None):
        """
        Los datos de la cola no estan pickleados pero si son binary.
        Hay que decodificarlos
        """
        self.logger.debug("")
        
        d_rsp = self.repo.lpop(qname, count)
        
        if d_rsp.get('status_code',0) == 200:
            l_datos = d_rsp['l_datos']
            l_datos = [ x.decode() for x in l_datos ]
            d_rsp = {'status_code':200, 'l_datos': l_datos}

        return d_rsp
    
    def rpop(self, qname=None, count=None):
        """
        Los datos de la cola no estan pickleados pero si son binary.
        Hay que decodificarlos
        """
        self.logger.debug("")
        
        d_rsp = self.repo.rpop(qname, count)
        
        if d_rsp.get('status_code',0) == 200:
            l_datos = d_rsp['l_datos']
            l_datos = [ x.decode() for x in l_datos ]
            d_rsp = {'status_code':200, 'l_datos': l_datos}

        return d_rsp
           
    def lpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.lpush(qname, payload)
        if d_rsp.get('status_code',0) == 200:
            d_rsp = {'status_code':200, 'queue_name': qname}
        
        return d_rsp
    
    def rpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.rpush(qname, payload)
        if d_rsp.get('status_code',0) == 200:
            d_rsp = {'status_code':200, 'queue_name': qname}
        
        return d_rsp
    
    def dequeue_rxlines(self, count=None):
        """
        Desencola count elementos de la cola RXDATA_QUEUE
        Los datos de la cola vienen pickeados.
        Los devuelvo como json
        """
        self.logger.debug("")

        d_rsp = self.repo.dequeue_rxlines(count)

        if d_rsp.get('status_code',0) == 200:

            l_pk_datastruct = d_rsp['l_pk_datastruct']

            # Des-serializo los elementos de la lista.
            try:
                l_datastruct = [ pickle.loads(element) for element in l_pk_datastruct ]
                d_rsp = {'status_code':200, 'l_datastruct': l_datastruct }
                
            except Exception as e:
                self.logger.error( f"QueueService:dequeue_rxlines: {e}")
                d_rsp = {'status_code':502, 'msg':f"{e}"}
                
        #
        return d_rsp

