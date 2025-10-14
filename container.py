#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

from dependency_injector import containers, providers

from servicios.ping_service import PingService
from servicios.config_service import ConfigService
from servicios.deletercd_service import DeleteRcdService
from servicios.ordenes_service import OrdenesService
from servicios.ordenesplc_service import OrdenesPlcService
from servicios.queue_service import QueueService
from servicios.uid2id_service import Uid2IdService
from servicios.dataline_service import DatalineService
from servicios.connectionstats_service import ConnectionStatsService
from servicios.loglevel_service import LogLevelService

from repositorios.reporedis import RepoRedis

from datasources.apibdredis import ApiBdRedis

from utilidades.login_config import configure_logger

from config import settings

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        modules=["resources.ping_resource",
                 "resources.help_resource",
                 "resources.deletercd_resource",
                 "resources.config_resource",
                 "resources.dequeuerxlines_resource",
                 "resources.uid2id_resource",
                 "resources.ordenes_resource",
                 "resources.dataline_resource",
                 "resources.ordenesplc_resource",
                 "resources.connectionstats_resource",
                 "resources.rxdataqueuelength_resource",
                 "resources.loglevel_resource",
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
    deletercd_service = providers.Factory(DeleteRcdService, repositorio=repo, logger=logger)
    config_service = providers.Factory(ConfigService, repositorio=repo, logger=logger)
    queue_service = providers.Factory(QueueService, repositorio=repo, logger=logger)
    uid2id_service = providers.Factory(Uid2IdService, repositorio=repo, logger=logger)
    ordenes_service = providers.Factory(OrdenesService, repositorio=repo, logger=logger)
    dataline_service = providers.Factory(DatalineService, repositorio=repo, logger=logger)
    ordenesplc_service = providers.Factory(OrdenesPlcService, repositorio=repo, logger=logger)
    connectionstats_service = providers.Factory(ConnectionStatsService, repositorio=repo, logger=logger)
    loglevel_service = providers.Factory(LogLevelService, logger=logger)




