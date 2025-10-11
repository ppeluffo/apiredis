#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python3

import os

#
BDREDIS_HOST = os.environ.get('BDREDIS_HOST','127.0.0.1')
BDREDIS_PORT = os.environ.get('BDREDIS_PORT','6379')
BDREDIS_DB = os.environ.get('BDREDIS_DB','0')

API_VERSION = os.environ.get('API_VERSION','R002 @ 2025-09-30')

# DEBUG->INFO->ERROR
LOG_LEVEL = os.environ.get('LOG_LEVEL','INFO')

# API_TESTING
API_TEST_HOST = "127.0.0.1"
API_TEST_PORT = "5100"
API_URL_BASE = f"http://{API_TEST_HOST}:{API_TEST_PORT}/apiredis/"