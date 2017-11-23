class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_sqr_sum(n):
            sum = 0
            while n:
                temp = n % 10
                sum += temp * temp
                n = n // 10
            return sum

        slow = n
        fast = n
        while 1:
            slow = digit_sqr_sum(slow)
            fast = digit_sqr_sum(fast)
            fast = digit_sqr_sum(fast)
            if slow == fast:
                break
        return slow == 1