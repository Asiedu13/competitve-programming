def squareNumbersLessThanN(n):
    if n > 0 and n < 21:
        for i in range(n):
            print(i ** 2)
        

if __name__ == '__main__':
    n = int(input())
    squareNumbersLessThanN(n)