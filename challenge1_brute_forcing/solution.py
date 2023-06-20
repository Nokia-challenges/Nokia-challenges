from utils import *

import requests

def run():
    response=requests.get(
        "https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt")
    )
    miofile=open("passphrase.txt","w")
    parole_attaccate=response.content
    parole=parole_attaccate.splitlines()
    for parola in parole:
        parola=str(parola)
        parola=parola[2:-1:]
        if check_password(parola):
            print(parola)
            miofile.write(parola)





if __name__ == "__main__":
    run()
