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
         
    def pop(self, qname=None, count=None):
        """
        """
        self.logger.debug("")
        return self.datasource.pop(qname, count)
    
    def push(self, qname=None, payload=None):
        """
        """
        self.logger.debug("")
        return self.datasource.push(qname, payload)
    
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
    
    def get_dataline(self, unit=None):
        """
        """
        self.logger.debug("")
        return self.datasource.get_dataline(unit)
    
    def put_alldata(self, unit=None, pk_d_alldata=None):
        """
        """
        self.logger.debug("")
        return self.datasource.put_alldata(unit, pk_d_alldata)
    
    def put_dataline(self, unit=None, pk_dataline=None):
        """
        """
        self.logger.debug("")
        return self.datasource.put_dataline(unit, pk_dataline)
    
    def put_timestamp(self, unit=None, pk_timestamp=None):
        """
        """
        self.logger.debug("")
        return self.datasource.put_timestamp(unit, pk_timestamp)