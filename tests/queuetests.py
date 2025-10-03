#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/queuelength"

def queuelength_test(qname=None):
    
    params = {'qname':qname}
    r = requests.get(URL, params=params)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("Queue Length Test: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Queue Length Test: Response FAIL")
        return False


if __name__ == '__main__':


    print("\nQueue Test....")
    queuelength_test(qname="LOG_QUEUE")
