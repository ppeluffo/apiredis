#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/delete"

def delete_test(dlgid="SPQTEST"):
    
    params = { 'unit':dlgid}
    r = requests.delete(URL, params=params)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("Delete Test: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Delete Test: Response FAIL")
        return False


if __name__ == '__main__':


    print("\nDelete Test....")
    delete_test("SPQTEST")
