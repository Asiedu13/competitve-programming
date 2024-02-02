class Solution(object):
    def smallestEvenMultiple(self, n):
        limit = 2 * n
        smallestMultiple = 0
        count = 1
        while count < limit:
            if count % n == 0 and count % 2 == 0:
                smallestMultiple = count
                break
            else:
                count += 1
        if smallestMultiple > 0:
            return smallestMultiple
        else:
            return limit


        