from utils import check_password


def run():
    dizionario = open("660000_parole_italiane.txt", "r")
    passphrase = open("passphrase.txt", "w")

    for parola in dizionario.readlines():
        parola = parola[0:-1]

        if check_password(parola):

            print(parola)

            passphrase.write(parola)
            return 0


if __name__ == "__main__":
    run()
