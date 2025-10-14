#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.uid2id_service import Uid2IdService


class Uid2IdResource(Resource):

    @inject
    def __init__(self, service: Uid2IdService = Provide[Container.uid2id_service], logger = Provide[Container.logger]):
        self.uid2id_service = service
        self.logger = logger

    def get(self):
        """
        Devuelve el par UID/ID en un json
        Invocacion: /apiredis/uid2id?unit=DLGID

        Testing:
        req=requests.get('http://127.0.0.1:5100/apiredis/uid2id',params={'uid':'UID'})
        json.loads(req.json())
            {'id':'DLGTEST','uid':'01234567'}

        """
        self.logger.debug("")

        parser = reqparse.RequestParser()
        parser.add_argument('uid',type=str,location='args',required=True)
        args=parser.parse_args()
        uid = args['uid']

        d_rsp = self.uid2id_service.get_id_from_uid(uid)
        assert isinstance(d_rsp, dict)

        status_code = d_rsp.pop('status_code', 0)
    
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 200:
            id = d_rsp.get('id', None)
            d_rsp = {'id':id }
        elif status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = {}
    
        return d_rsp, status_code  
       
        
    def put(self):
        """
          Actualiza(override) las tupla UID/DLGID
            Invocacion: apiredis/uid2id?
            Como es PUT, la orden la mandamos en un json {'uid':UID, 'unit': ID }

            Testing:
            d={'uid':'012345678', 'unit':'DLGTEST'}
            jd=json.dumps(d)
            req=requests.put('http://127.0.0.1:5100/apiredis/uid2id?, json=jd)
            json.loads(req.json())

        """
        self.logger.debug("")
        #
        parser = reqparse.RequestParser()
        parser.add_argument('uid',type=str,location='json',required=True)
        parser.add_argument('id',type=str,location='json',required=True)
        args=parser.parse_args()
        uid = args['uid']
        id = args['id']

        assert isinstance(uid, str)
        assert isinstance(id, str)

        d_rsp = self.uid2id_service.set_id_and_uid(uid, id)
        
        assert isinstance(d_rsp, dict)
        
        status_code = d_rsp.pop('status_code', 500)
        # No mando detalles de los errores en respuestas x seguridad.
        if status_code == 502:
            d_rsp = {'msg':"SERVICIO NO DISPONIBLE TEMPORALMENTE"}
        else:
            d_rsp = {}
    
        return d_rsp, status_code  
    
