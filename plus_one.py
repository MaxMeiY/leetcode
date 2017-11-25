class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        ha
        """
        res = ''
        for i in digits:
            res = res + str(i)
        res = str(int(res) + 1)
        return list(map(int, res))
        