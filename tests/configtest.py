#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = "http://127.0.0.1:5100/apiredis/config"

def config_test_get(dlgid="SPQTEST"):
    
    payload = {'unit': dlgid}
    r = requests.get(URL, params=payload)
    jdr = r.json()
    if r.status_code == 200:
        print("Config Test GET: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Config Test GET: Response FAIL")
        return False

def config_test_put( dlgid="SPQTEST"):
    
    params = {'unit': dlgid}
    payload = {
    "ANALOGS": {
        "A0": {
            "ENABLE": "TRUE",
            "IMAX": "20",
            "IMIN": "4",
            "MMAX": "10",
            "MMIN": "0",
            "NAME": "HTQ",
            "OFFSET": "0"
        },
        "A1": {
            "ENABLE": "FALSE",
            "IMAX": "20",
            "IMIN": "4",
            "MMAX": "10",
            "MMIN": "0",
            "NAME": "X",
            "OFFSET": "0"
        },
        "A2": {
            "ENABLE": "FALSE",
            "IMAX": "20",
            "IMIN": "4",
            "MMAX": "10",
            "MMIN": "0",
            "NAME": "X",
            "OFFSET": "0"
        }
    },
    "BASE": {
        "ALMLEVEL": "10",
        "FIRMWARE": "4.0.0a",
        "SAMPLES": "1",
        "PWRS_HHMM1": "1800",
        "PWRS_HHMM2": "1440",
        "PWRS_MODO": "0",
        "TDIAL": "900",
        "TPOLL": "30"
    },
    "COUNTERS": {
        "C0": {
            "ENABLE": "TRUE",
            "MAGPP": "0.01",
            "NAME": "q0",
            "MODO": "CAUDAL"
        },
        "C1": {
            "ENABLE": "FALSE",
            "MAGPP": "0.01",
            "NAME": "X",
            "MODO": "CAUDAL"
        }
    },
    "MODBUS": {
        "ENABLE": "TRUE",
        "LOCALADDR": "1",
        "M0": {
            "ENABLE": "TRUE",
            "NAME": "CAU0",
            "SLA_ADDR": "2",
            "ADDR": "2069",
            "NRO_RECS": "2",
            "FCODE": "3",
            "TYPE": "FLOAT",
            "CODEC": "C1032",
            "POW10": "0"
        },
        "M1": {
            "ENABLE": "FALSE",
            "NAME": "X",
            "SLA_ADDR": "2",
            "ADDR": "2069",
            "NRO_RECS": "2",
            "FCODE": "3",
            "TYPE": "FLOAT",
            "CODEC": "C1032",
            "POW10": "0"
        },
        "M2": {
            "ENABLE": "FALSE",
            "NAME": "X",
            "SLA_ADDR": "2",
            "ADDR": "2069",
            "NRO_RECS": "2",
            "FCODE": "3",
            "TYPE": "FLOAT",
            "CODEC": "C1032",
            "POW10": "0"
        },
        "M3": {
            "ENABLE": "FALSE",
            "NAME": "X",
            "SLA_ADDR": "2",
            "ADDR": "2069",
            "NRO_RECS": "2",
            "FCODE": "3",
            "TYPE": "FLOAT",
            "CODEC": "C1032",
            "POW10": "0"
        },
        "M4": {
            "ENABLE": "FALSE",
            "NAME": "X",
            "SLA_ADDR": "2",
            "ADDR": "2069",
            "NRO_RECS": "2",
            "FCODE": "3",
            "TYPE": "FLOAT",
            "CODEC": "C1032",
            "POW10": "0"
        }
    }
    }

    r = requests.put(URL, params=params, json=payload)
    jdr = r.json()
    if r.status_code == 200:
        print("Config Test PUT: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Config Test PUT: Response FAIL")
        return False

if __name__ == '__main__':

    print("\nConfig Test....")
    config_test_put("SPQTEST")
    config_test_get("SPQTEST")
