#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/ping"

def ping_test():
    
    r = requests.get(URL)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("Ping Test: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Ping Test: Response FAIL")
        return False


if __name__ == '__main__':


    print("\nPing Test....")
    ping_test()
