from utils import check_password


def run():
    """
    Reads the italian dictionary line by line, 
    strips the line and checks if it corresponds with the hash.
    """
    with open("660000_parole_italiane.txt") as file:
        for line in file:
            if check_password(line[:-1]):
                return line[:-1]
            


if __name__ == "__main__":
    run()
