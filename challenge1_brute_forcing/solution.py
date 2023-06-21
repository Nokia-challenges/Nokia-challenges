import utils


def run():
    with open("660000_parole_italiane.txt", "r") as f:
        for line in f:
            if utils.check_password(line[:-1]):
                with open("passphrase.txt", "w") as f:
                    f.write(line[:-1])
                break


if __name__ == "__main__":
    run()
