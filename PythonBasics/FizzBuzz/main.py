class Solution(object):
    def fizzBuzz(self, n):
        resultArr = []
        for i in range(1, n + 1):
            if (i % 3 == 0 and i % 5 == 0):
                resultArr.append('FizzBuzz')
            elif (i % 3 == 0 ):
                resultArr.append('Fizz')
            elif (i % 5 == 0):
                resultArr.append('Buzz')
            else:
                resultArr.append(str(i))
        return resultArr
    