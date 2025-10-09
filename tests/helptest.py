#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

import requests

URL = URL = "http://127.0.0.1:5100//apiredis/help"

def help_test():
    
    r = requests.get(URL)
    jdr = r.json()
    if r.status_code == 200:
        print("Help Test: Response OK")
        print(f"JSON={jdr}")
        return True
    else:
        print("Help Test: Response FAIL")
        return False


if __name__ == '__main__':


    print("\nHelp Test....")
    help_test()
