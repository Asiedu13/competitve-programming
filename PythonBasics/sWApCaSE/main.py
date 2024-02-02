def swap_case(s):
    word = s
    swappedCase = ''
    for i in range(len(word)):
        if word[i].islower():
            swappedCase += word[i].upper()
        else:
            swappedCase += word[i].lower()
    return swappedCase

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)