def run(s):

    stringamax=""
    for i in range(len(s)):
        for j in range(min(i+1, len(s)-i+1)):
            stringa=s[i-j:i+j+1:]
            if stringa==stringa[::-1]:
                if len(stringa)>len(stringamax):
                    stringamax=stringa

    for i in range(len(s)):
        if i>0:
            b=i
            e=i+1
            while b>=0 and e<len(s):
                stringa=s[b:e+1]
                if stringa==stringa[::-1] and len(stringa)>len(stringamax):
                    stringamax=stringa
                b-=1
                e+=1
        if i<len(s)-1:
            b=i-1
            e=i
            while b>=0 and e<len(s):
                stringa=s[b:e+1]
                if stringa==stringa[::-1] and len(stringa)>len(stringamax):
                    stringamax=stringa
                b-=1
                e+=1

    return stringamax


if __name__ == "__main__":
    run(s="nokiaikchallenges")
