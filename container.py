#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from dependency_injector import containers, providers

from servicios.pingservice import PingService
from servicios.debugidservice import DebugIdService
from servicios.deletercdservice import DeleteRcdService
from servicios.configservice import ConfigService
from servicios.queueservice import QueueService
from servicios.uid2idservice import Uid2IdService
from servicios.ordenesservice import OrdenesService
from servicios.datalineservice import DatalineService

from repositorios.reporedis import RepoRedis

from datasources.apibdredis import ApiBdRedis

from utilidades.login_config import configure_logger

from config import settings

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        modules=["resources.pingresource",
                 "resources.helpresource",
                 "resources.testresource",
                 "resources.debugidresource",
                 "resources.deletercdresource",
                 "resources.configresource",
                 "resources.queuelengthresource",
                 "resources.logqueuepopresource",
                 "resources.logqueuepushresource",
                 "resources.queuepopresource",
                 "resources.queuepushresource",
                 "resources.uid2idresource",
                 "resources.ordenesresource",
                 "resources.datalineresource"
                 ]
    )
    
    # Logger (singleton compartido)
    logger = providers.Singleton(configure_logger, name="api-redis")

    # Datasources
    ds_redis = providers.Factory(ApiBdRedis, logger=logger )
    
    # Repositorios
    repo = providers.Factory(RepoRedis,datasource=ds_redis, logger=logger)
    
    # Servicios
    ping_service = providers.Factory(PingService, repositorio=repo, logger=logger)
    debugid_service = providers.Factory(DebugIdService, repositorio=repo, logger=logger)
    deletercd_service = providers.Factory(DeleteRcdService, repositorio=repo, logger=logger)
    config_service = providers.Factory(ConfigService, repositorio=repo, logger=logger)
    queue_service = providers.Factory(QueueService, repositorio=repo, logger=logger)
    uid2id_service = providers.Factory(Uid2IdService, repositorio=repo, logger=logger)
    ordenes_service = providers.Factory(OrdenesService, repositorio=repo, logger=logger)
    dataline_service = providers.Factory(DatalineService, repositorio=repo, logger=logger)



