#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/ordenes"

def ordenes_test_get(dlgid=None):
    
    params = { 'unit': dlgid }
    r = requests.get(URL, params=params)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("Ordenes Test GET: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Ordenes Test GET: Response FAIL")
        return False

def ordenes_test_put( dlgid=None, ordenes=None):
    
    params = { 'unit': dlgid }
    payload = {"ordenes": ordenes }
    r = requests.put(URL, params=params, json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("Ordenes Test PUT: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Ordenes Test PUT: Response FAIL")
        return False

if __name__ == '__main__':

    print("\nDebugId Test....")
    ordenes_test_put("SPQTEST","RELOAD VALVE")
    ordenes_test_get("SPQTEST")
