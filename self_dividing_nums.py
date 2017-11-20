class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        haha
        """
        result = []
        for x in range(left, right+1):
            divisible = True
            for digit in str(x):
                if digit == '0' or x % int(digit) != 0:
                    divisible = False
            if divisible:
                result.append(x)
        return result
