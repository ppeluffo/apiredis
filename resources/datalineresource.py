#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.datalineservice import DatalineService

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
        d_rsp = self.dataline_service.get_dataline(unit)
        
        return d_rsp, 200
 
    def put(self):
        """
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
        parser.add_argument('dataline',type=str,location='json',required=True)
        args=parser.parse_args()
        unit = args['unit']
        unit_type = args['type']
        d_dataline = args['dataline']

        d_rsp = self.dataline_service.put_dataline(unit, unit_type, d_dataline)
        
        return d_rsp, 200
    