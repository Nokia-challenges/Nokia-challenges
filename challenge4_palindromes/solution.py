def run(s):
    palindroma=""

    for i in range(1,len(s)-1):
        if s[i-1]==s[i+1]:
            pos=i
            palindroma=s[pos-1]+s[pos]+s[pos+1]

    for j in range(2,len(s)):
        if s[pos-j]==s[pos+j]:
            palindroma=s[pos-j]+palindroma+s[pos+j]
        if s[pos-j]!=s[pos+j]:
            break

    print(palindroma)


if __name__ == "__main__":
    run(s="nokiaikchallenges")
