def run(s):
    palindroma=""

    for i in range(1,len(s)-1):
        if s[i-1]==s[i+1]:
            pos=i
            palindroma1=s[pos-1]+s[pos]+s[pos+1]

    for j in range(2,len(s)):
        if s[pos-j]==s[pos+j]:
            palindroma1=s[pos-j]+palindroma1+s[pos+j]
        if s[pos-j]!=s[pos+j]:
            break




    for h in range(len(s)-1):
        if s[h]==s[h+1]:
            pos=h
            palindroma2=s[pos]+s[pos+1]

    for k in range(1,len(s)):
        if s[pos-k]==s[pos+k+1]:
            palindroma2=s[pos-k]+palindroma2+s[pos+k+1]
        if s[pos-k]!=s[pos+k+1]:
            break


    if len(palindroma1)>len(palindroma2):
        print(palindroma1)
    elif len(palindroma2)>len(palindroma1):
        print(palindroma2)


if __name__ == "__main__":
    run(s="nokiaikchallenges")
