from operator import truediv

from utils import check_password


def run():
    f = open("660000_parole_italiane_ok.txt")
    f2 = open("passphrase.txt", "w")

    for pwd in f.readlines():
        pwd = pwd[0:-1]

        if check_password(pwd):
     
            f2.write(pwd)
            return 0


if __name__ == "__main__":
    run()
