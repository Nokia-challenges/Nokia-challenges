
def run(s):

    parola=""
    lenmax=0
    for i in range(len(s)):
        parola=s[i]
        for j in range(i+1,len(s)):
            parola=parola+s[j]
            if parola==parola[::-1]:
                if len(parola)>lenmax:
                    palindroma=parola
                    lenmax=len(parola)


    return palindroma


if __name__ == "__main__":
    run(s="nokiaikchallenges")
