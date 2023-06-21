import urllib.request

#url = "https://github.com/napolux/paroleitaliane/blob/master/paroleitaliane/660000_parole_italiane.txt"
from utils import check_password


def run():
    with urllib.request.urlopen('https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt') as response:
        while True:
            parola = response.readline()
            riga = parola.decode()
            riga = riga.rstrip()
            if check_password(riga) == True:
                print(riga)
                file_uno = open("passphrase.txt", "w")
                file_uno.write(riga)
                file_uno.close()
                break

    pass


if __name__ == "__main__":
    run()

