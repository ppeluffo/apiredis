#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import datetime as dt
import pickle


class DatalineService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_dataline(self, unit):
        """
        En la redis la configuracion es un dict serializado. 
        """
        self.logger.debug("")

        d_rsp = self.repo.get_dataline(unit)
    
        if d_rsp.get('rsp','ERR') == 'OK':
            pk_dataline = d_rsp['pk_dataline']
            if pk_dataline is None:
                dataline = None
            else:
                try:
                    dataline = pickle.loads(pk_dataline) 
                except Exception:
                    return {'rsp':'ERR', 'msg': 'pickle loads error'}
            d_rsp = {'rsp':'OK', 'dataline':dataline}
            return d_rsp

    def put_dataline(self, unit=None, unit_type=None, d_dataline=None):
        """
        """
        self.logger.debug("")

        # Timestamp.
        timestamp = dt.datetime.now()
        try:
            pk_timestamp = pickle.dumps(timestamp)
        except Exception as e:
            return { 'rsp':'ERR', 'msg': 'pickle error con timestamp'}
        #
        # pk_dataline:
        try:
            pk_dataline = pickle.dumps(d_dataline)
        except Exception as e:
            return { 'rsp':'ERR', 'msg': 'pickle error con dataline'}
        #
        # pk_alldata
        d_alldata = {'TYPE':unit_type, 'ID':'unit', 'D_LINE':d_dataline}
        try:
            pk_d_alldata = pickle.dumps(d_alldata)
        except Exception:
            d_rsp = {'rsp':'ERR', 'msg':'pickle dumps error'}
            return d_rsp
        #
        # Guardamos todos los datos en la redis ( cola general de datos )
        d_rsp = self.repo.put_alldata(unit, pk_d_alldata)
        if d_rsp.get('rsp','ERR') == 'ERR':
            return d_rsp
        
        # Guardamos la dataline en la redis (cola del datalogger)
        d_rsp = self.repo.put_dataline(unit, pk_dataline)
        if d_rsp.get('rsp','ERR') == 'ERR':
            return d_rsp

        # Guardamos el timestamp
        d_rsp = self.repo.put_timestamp(unit, pk_timestamp)
        if d_rsp.get('rsp','ERR') == 'ERR':
            return d_rsp
        
        return d_rsp
