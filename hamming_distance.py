class Solution:
    def hammingDistance(self, x, y):
        '''
        :type x: int
        :type y: int
        :rtype: int
        '''
        return (x ^ y).count('1')