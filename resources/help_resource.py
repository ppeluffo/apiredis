#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container

class HelpResource(Resource):

    @inject
    def __init__(self, logger = Provide[Container.logger]):
        self.logger = logger

    def get(self):
        ''' Retorna la descripcion de los metodos disponibles
        '''
        self.logger.debug("")
        
        d_rsp = {
            'GET /apiredis/ping': 'Indica el estado de la api.',
            'DELETE /apiredis/delete?unit=DLGID':'Borra la configuracion de la unit',
            'GET /apiredis/debugid': 'Retorna el unitID usado para debug',
            'PUT /apiredis/debugid': 'Setea el unitID usado para debug',
            'GET /apiredis/config?unit=DLGID':'Retorna la configuracion de la unit',
            'PUT /apiredis/config?unit=DLGID': 'Actualiza la configuracion de la unit',
            'GET /apiredis/uid2id?uid=<uid>': 'Retorna el DLGID asociado al UID',
            'PUT /apiredis/uid2id?dlgid=<dlgid>&uid=<uid>': 'Actualiza el par ( DLGID, UID )',
            'GET /apiredis/ordenes?unit=DLGID': 'Retorna la linea de ordenes para unit',
            'PUT /apiredis/ordenes?unit=DLGID': 'Actualiza(override) la linea de ordenes (json PUT Body) para unit',
            'GET /apiredis/dataline?unit=DLGID': 'Retorna diccionario con datos de ultima linea recibida',
            'PUT /apiredis/dataline?unit=DLGID': 'Actualiza los datos de ultima linea recibida (json PUT Body) y el timestamp',
            'GET /apiredis/queuelength?qname=<qn>': 'Devuelve el la cantidad de elementos de la cola',
            'GET /apiredis/queueitems?qname=<qn>&<count=nn>':'Devuelve count elementos de la cola',
        }
        return d_rsp , 200