from operator import truediv

from utils import check_password


def run():
    f = open("660000_parole_italiane_ok.txt")
    f2 = open("passphrase.txt", "w")

    for password in f.readlines():
        
        password = password[:-1]
#        print(password)

        if check_password(password):
            f2.write(password)
            return 0;



if __name__ == "__main__":
    run()

