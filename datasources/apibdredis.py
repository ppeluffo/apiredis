#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
Todas las funciones de la API responde con un diccionario d_res
El campo 'rsp' SIEMPRE ESTA PRESENTE y puede estar en 'OK' o en 'ERR'.
"""

import redis
from config import settings

class ApiBdRedis:

    def __init__(self, logger):
        self.logger = logger
        self.rh = redis.Redis( settings.BDREDIS_HOST, settings.BDREDIS_PORT,settings.BDREDIS_DB, socket_connect_timeout=1)
        
    def ping(self):
        """
        Si el server responde, el ping da True.
        Si no responde, sale por exception.
        """
        #self.logger.info("TESTING LOGGER INFO")
        #self.logger.debug("TESTING LOGGER DEBUG")
        #self.logger.error("TESTING LOGGER ERROR")

        self.logger.debug(f"")

        try:
            self.rh.ping()
            d_rsp = {'rsp':'OK',
                     'version':settings.API_VERSION,
                     'REDIS_HOST':settings.BDREDIS_HOST,
                     'REDIS_PORT': settings.BDREDIS_PORT }
            return d_rsp
        
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp

    def read_debugid(self):
        """
        la respuesta del hget es un binary string o None.
        """
        self.logger.debug(f"")
        try:
            debug_id = self.rh.hget('SPCOMMS', 'DEBUG_ID')
            d_rsp = {'rsp':'OK',
                     'debugid':debug_id }
            return d_rsp
    
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
    
    def set_debugid(self, debugid=None):
        """
        """
        self.logger.debug(f"")
        try:
            _ = self.rh.hset('SPCOMMS', 'DEBUG_ID', debugid )
            return {'rsp':'OK'}
        
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp

    def delete_unit(self, unit=None):
        """
        """
        self.logger.debug(f"")
        try:
            _= self.rh.delete(unit)
            return {'rsp':'OK'}
        
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp

    def read_config(self, unit=None):
        """
        """
        self.logger.debug(f"")            
        try:
            pkconfig = self.rh.hget( unit, 'PKCONFIG')
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        if pkconfig is None:
            #app.logger.info( f'(004) ApiREDIS_WARN001: No configuration rcd')
            return {'rsp':'ERR', 'msg':'pkconfig is None'}
        else:
            return {'rsp':'OK', 'pkconfig':pkconfig}
        
    def update_config(self, unit=None, pkconfig=None):
        """
        """
        self.logger.debug(f"")
        try:
            _ = self.rh.hset( unit,'PKCONFIG', pkconfig)
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return {'rsp':'OK'}

    def get_length(self, qname=None):
        """
        """
        self.logger.debug(f"")

        try:
            qlength = self.rh.llen(qname)
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        d_rsp =  {'rsp':'OK', 'qname':qname, 'length':qlength}
        return d_rsp

    def pop(self, qname=None, count=None):
        """
        Si la lista no existe, redis devuelve un None.
        Si la lista existe y está vacia, devuelve None.
        A priori no sabemos si los datos de la lista estan o no pickleados
        """
        self.logger.debug(f"")

        l_pkdatos = []
        try:
            l_datos = self.rh.lpop(qname, count)
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        d_rsp = { 'rsp':'OK', 'l_datos':l_datos }
        #self.logger.debug(f"d_rsp={d_rsp}")
        return d_rsp

    def push(self, qname=None, payload=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.rpush( qname, payload)
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return d_rsp
    
    def get_id_from_uid(self, uid=None):

        self.logger.debug(f"")

        try:
            id = self.rh.hget('RECOVERIDS', uid )
            d_rsp = {'rsp':'OK', 'uid': uid, 'id':id }
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return d_rsp
    
    def set_id_and_uid(self, uid=None, id=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset( 'RECOVERIDS', uid,id )
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        
        return d_rsp

    def get_ordenes(self, unit=None):
        """
        """
        self.logger.debug(f"")

        try:
            pk_ordenes = self.rh.hget( unit, 'PKORDENES' )
            d_rsp = {'rsp':'OK', 'pk_ordenes':pk_ordenes}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp

        return d_rsp

    def set_ordenes(self, unit=None, pk_ordenes=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset(unit, 'PKORDENES', pk_ordenes )
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return d_rsp
    
    def get_dataline(self, unit=None):
        """
        """
        self.logger.debug(f"")

        try:
            pk_dataline = self.rh.hget( unit, 'PKLINE')
            d_rsp = {'rsp':'OK', 'pk_dataline':pk_dataline }
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return d_rsp
    
    def put_alldata(self, unit=None, pk_d_alldata=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.rpush( 'RXDATA_QUEUE', pk_d_alldata)
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        # 
        return d_rsp
 
    def put_dataline(self, unit=None, pk_dataline=None):
        """
        """
        self.logger.debug("")

        try:
            _ = self.rh.hset( unit, 'PKLINE', pk_dataline )
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        #
        return d_rsp
    
    def put_timestamp(self, unit=None, pk_timestamp=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset( 'TIMESTAMP', unit, pk_timestamp )
            d_rsp = {'rsp':'OK'}
        except redis.ConnectionError:
            self.logger.error( "Redis ConnectionError")
            d_rsp = {'rsp':'ERR',  'msg':"Redis ConnectionError" }
            return d_rsp
        # 
        return d_rsp
