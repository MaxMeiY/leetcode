class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                x = 'FizzBuzz'
            elif i % 3 == 0:
                x = 'Fizz'
            elif i % 5 == 0:
                x = 'Buzz'
            else:
                x = str(i)
            result.append(x)
        return result
