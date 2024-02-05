class Solution(object):
    def finalValueAfterOperations(self, operations):
        x_value = 0

        for i in operations:
            if i == '--X' or i == "X--":
                x_value = x_value - 1
                print(x_value)
            elif i == "++X" or i == "X++":
                x_value = x_value + 1 
                print(x_value)
        return x_value