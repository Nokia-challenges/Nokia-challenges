from utils import check_password

def run():
    dizionario = open("660000_parole_italiane_ok.txt","r")
    f2 = open("passphrase.txt", "w")

    for parola in dizionario.readlines():
        parola=parola[0:-1]

        if check_password(parola):
            print(parola)

            f2.write(parola)
            return 0

    print("")
    pass


if __name__ == "__main__":
    run()
