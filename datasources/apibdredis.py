#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
Todas las funciones de la API responde con un diccionario d_res
El campo 'rsp' SIEMPRE ESTA PRESENTE y puede estar en 'OK' o en 'ERR'.

Respuestas a operaciones en REDIS:
https://redis.io/docs/latest/commands/

HSET:
    Bulk string reply: The value associated with the field.
    Null reply: If the field is not present in the hash or key does not exist.

HSET:
    Integer reply: the number of fields that were added.

DELETE:
    Integer reply: the number of keys that were removed.
    A key is ignored if it does not exist

LLEN:
    Integer reply: the length of the list. ( 0 si la lista no existe )

LPOP:
    Null reply: if the key does not exist.
    Bulk string reply: when called without the count argument, the value of the first element.
    Array reply: when called with the count argument, a list of popped elements.

LPUSH: 
    Integer reply: the length of the list after the push operation.

RPUSH:
    Integer reply: the length of the list after the push operation.


read_debugid: HGET : None('debugid') .hget('SPCOMMS', 'DEBUG_ID')
set_debugid: HSET:                   .hset('SPCOMMS', 'DEBUG_ID', debugid )

delete_unit: DEL:                    .delete(unit)

read_config: HGET: None('pkconfig')  .hget( unit, 'PKCONFIG')
update_config: HSET:                 .hset( unit,'PKCONFIG', pkconfig)

get_length: LLEN                     .llen(qname)
pop: LPOP: None ('l_datos')          .lpop(qname, count)
push: RPUSH                          .rpush(qname, payload)

get_id_from_uid: HGET : None('id')      .hget('RECOVERIDS', uid )
set_id_and_uid: HSET:                   .hset( 'RECOVERIDS', uid,id )

get_ordenes: HGET: None ('pk_ordenes')  .hget( unit, 'PKORDENES' )
set_ordenes: HSET:                      .hset(unit, 'PKORDENES', pk_ordenes )

get_dataline: HGET: ('pk_dataline')     .hget( unit, 'PKLINE')
put_dataline: HSET:                     .hset( unit, 'PKLINE', pk_dataline )

put_alldata:                         .rpush( 'RXDATA_QUEUE', pk_d_alldata)

put_timestamp: HSET:                 .hset( 'TIMESTAMP', unit, pk_timestamp )

*******************************************************************************************


En las colas, insertamos al final (RPUSH) y sacamos desde adelante (LPOP)
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
            ds_rsp = {'status_code': 200,
                      'version':settings.API_VERSION,
                      'REDIS_HOST':settings.BDREDIS_HOST,
                      'REDIS_PORT': settings.BDREDIS_PORT }
        
        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            ds_rsp = {'status_code': 502,  'msg':f"{e}" }
            
        return ds_rsp

    ########################################################################

    def delete_unit(self, unit=None):
        """
        """
        self.logger.debug(f"")
        try:
            _= self.rh.delete(unit)
            d_rsp = {'status_code': 200}
        
        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
            
        return d_rsp

    def read_config(self, unit=None):
        """
        La BD redis envia un string (datos pickleados)
        """
        self.logger.debug(f"")            
        try:
            pkconfig = self.rh.hget( unit, 'PKCONFIG')
            if pkconfig is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = {'status_code': 200, 'pkconfig':pkconfig}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
            
        return d_rsp
        
    def update_config(self, unit=None, pkconfig=None):
        """
        """
        self.logger.debug(f"")
        try:
            _ = self.rh.hset( unit,'PKCONFIG', pkconfig)
            d_rsp = {'status_code': 200}
        
        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }

        return d_rsp

    ########################################################################
 
    def get_id_from_uid(self, uid=None):

        self.logger.debug(f"")

        try:
            id = self.rh.hget('RECOVERIDS', uid )
            if id is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = {'status_code': 200, 'id':id }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def set_id_and_uid(self, uid=None, id=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset( 'RECOVERIDS', uid,id )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        
        return d_rsp

    ########################################################################

    def get_ordenes(self, unit=None):
        """
        Devuelve un string pickeado
        """
        self.logger.debug(f"")

        try:
            pk_ordenes = self.rh.hget( unit, 'PKORDENES' )
            if pk_ordenes is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = {'status_code': 200, 'pk_ordenes':pk_ordenes}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }

        return d_rsp

    def set_ordenes(self, unit=None, pk_ordenes=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset(unit, 'PKORDENES', pk_ordenes )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def delete_ordenes(self, unit=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hdel(unit, 'PKORDENES' )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
          
    def get_ordenesplc(self, unit=None):
        """
        """
        self.logger.debug(f"")

        try:
            pk_ordenes_plc = self.rh.hget( unit, 'PKATVISE' )
            if pk_ordenes_plc is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = {'status_code': 200, 'pk_ordenes_plc':pk_ordenes_plc}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }

        return d_rsp

    def set_ordenesplc(self, unit=None, pk_ordenes_plc=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset(unit, 'PKATVISE', pk_ordenes_plc )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def delete_ordenesplc(self, unit=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hdel(unit, 'PKATVISE' )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp

    ########################################################################

    def read_dataline(self, unit=None):
        """
        Lee el campo PKLINE del HSET de la unidad
        """
        self.logger.debug(f"")

        try:
            pk_dataline = self.rh.hget( unit, 'PKLINE')
            if pk_dataline is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = {'status_code': 200, 'pk_dataline':pk_dataline }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def save_dataline(self, unit=None, pk_dataline=None):
        """
        """
        self.logger.debug("")

        try:
            _ = self.rh.hset( unit, 'PKLINE', pk_dataline )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def save_timestamp(self, unit=None, pk_timestamp=None):
        """
        Los timestamps se ponen en un hash, con clave la unit, y picleados
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.hset( 'TIMESTAMP', unit, pk_timestamp )
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        # 
        return d_rsp
    
    def enqueue_dataline(self, unit=None, pk_datastruct=None):

        self.logger.debug(f"")

        try:
            _ = self.rh.rpush( 'RXDATA_QUEUE', pk_datastruct)
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        # 
        return d_rsp

    def read_timestamps(self):
        """
        Leo todo el hash TIMESTAMP.
        Las claves son las unit_id
        Los valores son los timestamps pickeados.
        La redis me da un diccionario.
        """
        self.logger.debug(f"")

        try:
            d_pk_timestamp = self.rh.hgetall( 'TIMESTAMP' )
            d_rsp = {'status_code': 200, 'd_pk_timestamp': d_pk_timestamp }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        # 
        return d_rsp       

    def dequeue_rxlines(self, count=None):
        """
        Si la lista no existe, redis devuelve un None.
        Si la lista existe y está vacia, devuelve None.
        """
        self.logger.debug(f"")

        try:
            l_pk_datastruct = self.rh.lpop('RXDATA_QUEUE', count)
            if l_pk_datastruct is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = { 'status_code': 200, 'l_pk_datastruct': l_pk_datastruct }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
            
    ########################################################################

    def get_length(self, qname=None):
        """
        """
        self.logger.debug(f"")

        try:
            qlength = self.rh.llen(qname)
            d_rsp =  {'status_code': 200, 'qname':qname, 'length':qlength}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp

    def lpop(self, qname=None, count=None):
        """
        Si la lista no existe, redis devuelve un None.
        Si la lista existe y está vacia, devuelve None.
        A priori no sabemos si los datos de la lista estan o no pickleados
        """
        self.logger.debug(f"")

        try:
            l_datos = self.rh.lpop(qname, count)
            if l_datos is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = { 'status_code': 200, 'l_datos':l_datos }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp

    def rpop(self, qname=None, count=None):
        """
        Si la lista no existe, redis devuelve un None.
        Si la lista existe y está vacia, devuelve None.
        A priori no sabemos si los datos de la lista estan o no pickleados
        """
        self.logger.debug(f"")

        try:
            l_datos = self.rh.rpop(qname, count)
            if l_datos is None:
                d_rsp = {'status_code': 404 }
            else:
                d_rsp = { 'status_code': 200, 'l_datos':l_datos }

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def rpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.rpush( qname, payload)
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp
    
    def lpush(self, qname=None, payload=None):
        """
        """
        self.logger.debug(f"")

        try:
            _ = self.rh.lpush( qname, payload)
            d_rsp = {'status_code': 200}

        except Exception as e:
            self.logger.error( f"Redis Error {e}")
            d_rsp = {'status_code': 502,  'msg':f"{e}" }
        #
        return d_rsp

