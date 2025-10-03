#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/debugid"

def debugid_test_get():
    
    r = requests.get(URL)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("DebugId Test GET: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("DebugId Test GET: Response FAIL")
        return False

def debugid_test_put( debugid="SPQTEST"):
    
    payload = {"debugid": debugid }
    r = requests.put(URL, json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("DebugId Test PUT: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("DebugId Test PUT: Response FAIL")
        return False

if __name__ == '__main__':

    print("\nDebugId Test....")
    debugid_test_put("SQPTEST")
    debugid_test_get()
