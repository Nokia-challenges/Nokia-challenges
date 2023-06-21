
def run(s):
    list = []

    if len(s)%2 != 0:
        for i in range(1, len(s)-1):
            conta = 1
            ris1 = ""
            ris = ""
            while True:
                if (i-conta) < 0 or (i+conta) > len(s):
                    break
                if s[i-conta] == s[i+conta]:
                    ris1 += s[i+conta]
                    conta = conta + 1
                else:
                    ris = ris1[::-1] + s[i] + ris1
                    break
            list.append(ris)
    else:
        for i in range(1, len(s) - 1):
            conta = 1
            ris1 = ""
            ris = ""
            if s[i] == s[i+1]:
                while True:
                    if (i - conta) < 0 or (i + conta + 1) > len(s):
                        break
                    if s[i - conta] == s[i + conta + 1]:
                        ris1 += s[i + conta]
                        conta = conta + 1
                    else:
                        ris = ris1[::-1] + ris1
                        break
                list.append(ris)


    max = 0

    for i in list:
        if len(i) > max:
            max = len(i)
            s = i

    return s


if __name__ == "__main__":
    run(s="nokiaikchallenges")
