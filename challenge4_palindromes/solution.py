def run(s):
    longest_word = s[0]
    longest_i = 0
    length = len(s)

    for index in range(length):
        for i in range(1, min(index+1, length-index)):
            if s[index-i] != s[index+i]:
                break
            elif i>longest_i:
                longest_i = i
                longest_word = s[index-i:index+i+1]

    return longest_word

if __name__ == "__main__":
    run(s="nokiaikchallenaaaaaaaaaaagesbbbbbbbbbbbbbbbbbbbbbb")
