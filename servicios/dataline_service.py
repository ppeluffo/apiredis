#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import datetime as dt
import pickle

class DatalineService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def read_dataline(self, unit):
        """
        En la redis la configuracion es un dict pickeado.
        Aqui lo des-pickleo
        """
        self.logger.debug("")

        d_rsp = self.repo.read_dataline(unit)

        if d_rsp.get('status_code',0) == 200:

            pk_dataline = d_rsp['pk_dataline']
            try:
                dataline = pickle.loads(pk_dataline) 
                d_rsp = {'status_code':200, 'dataline':dataline}

            except Exception as e:
                self.logger.error( f"DatalineService:read_dataline: {e}")
                d_rsp = {'status_code':502, 'msg':f"{e}"}

        return d_rsp

    def process_dataline(self, unit=None, unit_type=None, d_dataline=None):
        """
        Al recibir un dataline se hacen 3 funciones:
        - Se guarda en el HSET de la unidad
        - Se guarda el timestamp en el HSET TIMESTAMP. Este nos permite saber cuando llegaron el ultimo dato de c/unidad
        - Se guarda en una cola de datos recibidos RXDATA_QUEUE.
        """
        self.logger.debug("")

        # Timestamp: Indica la fecha/hora de recibido el dato.
        timestamp = dt.datetime.now()
        try:
            pk_timestamp = pickle.dumps(timestamp)
        except Exception as e:
            self.logger.error( f"DatalineService:process_dataline: {e}")
            d_rsp = {'status_code':502, 'msg':f"{e}"}
            return d_rsp
        #
        # pk_dataline: Los datos recibidos se guardan y encolan en forma serializada pickle
        d_payload = d_dataline.get('dataline',{})
        try:
            pk_dataline = pickle.dumps(d_payload)
        except Exception as e:
            self.logger.error( f"DatalineService:process_dataline: {e}")
            d_rsp = {'status_code':502, 'msg':f"{e}"}
            return d_rsp
        #
        # pk_datastruct: Estructura de datos serializada que se encola en RXDATA_QUEUE
        d_datastruct = {'TYPE':unit_type, 'ID':unit, 'D_LINE':d_payload}
        try:
            pk_datastruct = pickle.dumps(d_datastruct)
        except Exception as e:
            self.logger.error( f"DatalineService:process_dataline: {e}")
            d_rsp = {'status_code':502, 'msg':f"{e}"}
            return d_rsp
        #
        # Debemos hacer 3 operaciones en la redis:

        # 1. Guardamos los datos en el HSET de la unidad
        d_rsp = self.repo.save_dataline(unit, pk_dataline)
        if d_rsp.get('status_code',0) != 200:
            return d_rsp
        
        # 2. Guardamos el timestamp
        d_rsp = self.repo.save_timestamp(unit, pk_timestamp)
        if d_rsp.get('status_code',0) != 200:
            return d_rsp
        
        # 3. Encolo todos los datos en RXDATA_QUEUE para luego procesarlos y pasarlos a pgsql.
        d_rsp = self.repo.enqueue_dataline(unit, pk_datastruct)
        if d_rsp.get('status_code',0) != 200:
            return d_rsp
                
        return d_rsp
