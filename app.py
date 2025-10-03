#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python
"""
API REST para acceder a los servicios de REDIS del servidor de comunicaciones

"""

import logging
from config import settings

from resources import helpresource
from resources import pingresource
from resources import testresource
from resources import debugidresource
from resources import deletercdresource
from resources import configresource
from resources import queuelengthresource
from resources import logqueuepopresource
from resources import logqueuepushresource

from resources import queuepopresource
from resources import queuepushresource
from resources import uid2idresource
from resources import ordenesresource
from resources import datalineresource

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


    api.add_resource( pingresource.PingResource, '/apiredis/ping')
    api.add_resource( helpresource.HelpResource, '/apiredis/help')
    api.add_resource( testresource.TestResource, '/apiredis/test')
    api.add_resource( debugidresource.DebugIdResource, '/apiredis/debugid')
    api.add_resource( configresource.ConfigResource, '/apiredis/config')
    api.add_resource( deletercdresource.DeleteRcdResource, '/apiredis/delete')
    api.add_resource( ordenesresource.OrdenesResource, '/apiredis/ordenes')
    api.add_resource( queuelengthresource.QueueLengthResource, '/apiredis/queuelength')
    api.add_resource( logqueuepopresource.LogQueuePopResource, '/apiredis/logqueuepop')
    api.add_resource( logqueuepushresource.LogQueuePushResource, '/apiredis/logqueuepush')
    api.add_resource( queuepopresource.QueuePopResource, '/apiredis/queuepop') 
    api.add_resource( uid2idresource.Uid2IdResource, '/apiredis/uid2id')
    api.add_resource( datalineresource.DatalineResource, '/apiredis/dataline')

#    api.add_resource( queuepushresource.QueuePushResource, '/apiredis/queuepush')
#    api.add_resource( OrdenesAtvise, '/apiredis/ordenesatvise')
#    api.add_resource( LogQueuePop, '/apiredis/logqueuepop')
#    api.add_resource( LogQueueLength, '/apiredis/logqueuelength')
#    api.add_resource( Stats, '/apiredis/stats')
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

