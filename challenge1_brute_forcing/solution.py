from utils import *
import requests

def run():
    response = requests.get("https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt")

    parole_attaccate = response.content
    parole = parole_attaccate.splitlines()
    miofile=open("passphrase.txt","w")

    for i in range(len(parole)):
        if check_password(parole[i].decode())==True:
            miofile.write(parole[i].decode())





if __name__ == "__main__":
    run()
