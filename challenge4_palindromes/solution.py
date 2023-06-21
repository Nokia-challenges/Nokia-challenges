def run(s):
    longest_word = s[0]
    length = len(s)
    for index in range(length):
        for i in range(1, min(index+1, length-index)):
            if s[index-i] != s[index+i]:
                if s[index-i] != s[index]:
                    break
                elif len(palindrome:=s[index-i:index+i]) > len(longest_word):
                    longest_word = palindrome
                break
            elif len(palindrome:=s[index-i:index+i+1])>len(longest_word):
                longest_word = palindrome
    return s[-2:] if len(longest_word)<2 and s[-1]==s[-2] else longest_word

if __name__ == "__main__":
    run(s="ffdffffcefdd")
