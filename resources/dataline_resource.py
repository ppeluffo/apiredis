#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from flask import request
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.dataline_service import DatalineService
from utilidades.parse_to_dict import parse_to_dict

class DatalineResource(Resource):

    @inject
    def __init__(self, service: DatalineService = Provide[Container.dataline_service], logger = Provide[Container.logger]):
        self.dataline_service = service
        self.logger = logger

    def get(self):
        """
        Leemos la ultima linea que envio el datalogger.

        Testing:
        req=requests.get('http://127.0.0.1:5100/apiredis/dataline',params={'unit':'PABLO'})
        json.loads(req.json())
        {'DATE': '230519','TIME': '144412','HTQ': '-2.50','q0': '0.000','AI0': 'nan','QS': '0.000','bt': '12.480'}
        """
        self.logger.debug("")
        
        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args['unit']
        #
        d_rsp = self.dataline_service.read_dataline(unit)
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        d_dataline = d_rsp.get('dataline',{})

        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = d_dataline
    
        return d_rsp, status_code  
    

    def put(self):
        """
        Al recibir un dataline se hacen 3 funciones:
        - Se guarda en el HSET de la unidad
        - Se guarda el timestamp en el HSET TIMESTAMP. Este nos permite saber cuando llegaron el ultimo dato de c/unidad
        - Se guarda en una cola de datos recibidos RXDATA_QUEUE.

          Actualiza(override) la ultima linea eviada por la unidad.
            NO CHEQUEA EL FORMATO
            Como es PUT, la configuracion la mandamos en un json { dict_line }
            Encola la linea en RXDATA_QUEUE para su posterior procesamiento

            Testing:
            d_data = {'DATE': '230519','TIME': '144412','HTQ': '-2.50', 'q0': '0.000','AI0': 'nan','QS': '0.000','bt': '12.480'}
            j_data = json.dumps(data)
            req=requests.put('http://127.0.0.1:5100/apiredis/dataline', params={'unit':'DLGTEST','type':'PLCR3'}, json=j_data)
            json.loads(req.json())

        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('unit',type=str,location='args',required=True)
        parser.add_argument('type',type=str,location='args',required=True)
        args=parser.parse_args()
        unit = args.get('unit','')
        unit_type = args.get('type','')

        d_p = request.get_json()
        d_dataline = parse_to_dict(d_p)
        assert isinstance( d_dataline, dict )

        d_rsp = self.dataline_service.process_dataline(unit, unit_type, d_dataline)
        assert isinstance(d_rsp, dict)

        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = {}
    
        return d_rsp, status_code 
    