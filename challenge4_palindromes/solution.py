import math


def run(s):
    lunghezza = len(s)
    if lunghezza == 0:
        return ""
    offset = 0
    trovate = []
    while offset < lunghezza:
        analizzato = s[offset:]
        len_analizzato = len(analizzato)
        for i in range(len_analizzato, 0, -1):
            possibile = analizzato[:i]
            found = True
            for iter in range(0, math.ceil(len(possibile) / 2)):
                if possibile[iter] != possibile[-(iter + 1)]:
                    found = False
                    break
            if found:
                trovate.append(possibile)
        offset += 1

    highest = ""
    highest_len = 0
    for trovata in trovate:
        if len(trovata) > highest_len:
            highest = trovata
            highest_len = len(trovata)
    return highest


if __name__ == "__main__":
    run(s="nokiaikchallenges")
