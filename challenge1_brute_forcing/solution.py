import urllib.request

url = "https://github.com/napolux/paroleitaliane/blob/master/paroleitaliane/660000_parole_italiane.txt"
from utils import check_password


def run():
    with urllib.request.urlopen(url) as response:
        while True:
            html = response.readline()
            if check_password(html) == True:
                file_uno = open("passphrase.txt", "w")
                file_uno.write(html)
                file_uno.close()

    pass


if __name__ == "__main__":
    run()
