#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
API REST para acceder a los servicios de REDIS del servidor de comunicaciones

"""


import logging
from config import settings

from resources import help_resource
from resources import ping_resource
from resources import config_resource
from resources import deletercd_resource
from resources import ordenes_resource
from resources import ordenesplc_resource

from resources import uid2id_resource
from resources import dataline_resource
from resources import connectionstats_resource
from resources import dequeuerxlines_resource
from resources import rxdataqueuelength_resource
from resources import loglevel_resource

from container import Container

from flask import Flask
from flask_restful import Api

from utilidades.login_config import configure_logger

def create_app(gunicorn: bool = False):

    app = Flask(__name__)
    api = Api(app)

    container = Container()

    # Sobrescribir logger según modo
    container.logger.override(configure_logger("api-redis", gunicorn=gunicorn))
    """
    if gunicorn:
        container.logger.override(logging.getLogger("gunicorn.error"))
    else:
        container.logger.override(logging.getLogger("api-redis"))
    """

    container.init_resources()
    container.wire(modules=[__name__])


    api.add_resource( ping_resource.PingResource, '/apiredis/ping')
    api.add_resource( help_resource.HelpResource, '/apiredis/help')
    api.add_resource( loglevel_resource.LogLevelResource, '/apiredis/loglevel')
    api.add_resource( config_resource.ConfigResource, '/apiredis/config')
    api.add_resource( deletercd_resource.DeleteRcdResource, '/apiredis/delete')
    api.add_resource( ordenes_resource.OrdenesResource, '/apiredis/ordenes') 
    api.add_resource( ordenesplc_resource.OrdenesPlcResource, '/apiredis/ordenesplc')
    api.add_resource( uid2id_resource.Uid2IdResource, '/apiredis/uid2id')
    api.add_resource( dataline_resource.DatalineResource, '/apiredis/dataline')
    api.add_resource( connectionstats_resource.ConnectionStatsResource, '/apiredis/connectionstats')
    api.add_resource( dequeuerxlines_resource.DequeueRxLinesResource, '/apiredis/dequeuerxlines')
    api.add_resource( rxdataqueuelength_resource.RxDataQueueLengthResource, '/apiredis/rxdataqueuelength')
#    
    return app

# Lineas para cuando corre en gurnicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app = create_app(gunicorn=True)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info(f'Starting APIREDIS: REDIS_HOST={settings.BDREDIS_HOST}, REDIS_PORT={settings.BDREDIS_PORT}')


# Lineas para cuando corre en modo independiente
if __name__ == '__main__':
    app = create_app(gunicorn=False)
    app.run(host='0.0.0.0', port=5100, debug=True)

