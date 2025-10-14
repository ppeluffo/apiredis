#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python3


class RepoRedis:
    """
    Repositorio que se encarga de consultar la Redis
    """
    
    def __init__(self, datasource, logger):
        self.datasource = datasource
        self.logger = logger
        
    def ping(self):
        """
        """
        self.logger.debug("")
        return self.datasource.ping()
        
    def read_debugid(self):
        """
        """
        self.logger.debug("")
        return self.datasource.read_debugid()
    
    def set_debugid(self, debugid=None):
        """
        """
        self.logger.debug("")
        return self.datasource.set_debugid(debugid)
    
    def delete_unit(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.delete_unit(unit)
    
    def read_config(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.read_config(unit)

    def update_config(self, unit=None, pkconfig=None):
        """
        """
        self.logger.debug("")
        return self.datasource.update_config(unit, pkconfig)
        
    def get_length(self, qname=None):
        """
        """
        self.logger.debug("")
        return self.datasource.get_length(qname)
         
    def rpop(self, qname=None, count=None):
        """
        """
        self.logger.debug("")
        return self.datasource.rpop(qname, count)
    
    def lpop(self, qname=None, count=None):
        """
        """
        self.logger.debug("")
        return self.datasource.lpop(qname, count)
    
    def rpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        return self.datasource.rpush(qname, payload)
    
    def lpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        return self.datasource.lpush(qname, payload)
    
    def get_id_from_uid(self, uid=None):
        """
        """
        self.logger.debug("")
        return self.datasource.get_id_from_uid(uid)

    def set_id_and_uid(self, uid=None, id=None):
        """
        """
        self.logger.debug("")
        return self.datasource.set_id_and_uid(uid, id)
    
    def get_ordenes(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.get_ordenes( unit)  
    
    def set_ordenes(self, unit=None, pk_ordenes=None):
        """
        """
        self.logger.debug("")
        return self.datasource.set_ordenes(unit, pk_ordenes)
    
    def read_dataline(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.read_dataline(unit)
    
    def enqueue_dataline(self, unit=None, pk_datastruct=None):
        """
        """
        self.logger.debug("")
        return self.datasource.enqueue_dataline(unit, pk_datastruct)
    
    def dequeue_rxlines(self, count=None):
        """
        """
        self.logger.debug("")
        return self.datasource.dequeue_rxlines(count)

    def save_dataline(self, unit=None, pk_dataline=None):
        """
        """
        self.logger.debug("")
        return self.datasource.save_dataline(unit, pk_dataline)
    
    def save_timestamp(self, unit=None, pk_timestamp=None):
        """
        """
        self.logger.debug("")
        return self.datasource.save_timestamp(unit, pk_timestamp)
    
    def read_timestamps(self):
        """
        """
        self.logger.debug("")
        return self.datasource.read_timestamps()
    
    def get_ordenesplc(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.get_ordenesplc( unit) 
    
    def set_ordenesplc(self, unit=None, pk_ordenes_plc=None):
        """
        """
        self.logger.debug("")
        return self.datasource.set_ordenesplc(unit, pk_ordenes_plc)
    
    