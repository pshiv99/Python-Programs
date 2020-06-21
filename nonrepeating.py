def firstNonRepeatingCharacter(s: str):
    countCharacter = [0 for i in range(26)]

    for i in s:
        index = ord(i) - 97
        countCharacter[index] += 1

    for i in range((len(s))):
        if countCharacter[ord(s[i]) - 97] == 1 :
            return i
    
    return -1

if __name__ == '__main__':
    s = input()

    result = firstNonRepeatingCharacter(s)

    print(result, end='')