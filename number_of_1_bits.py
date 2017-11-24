class solution:
    def num_1_bit(self, n):
        '''
        :type: int
        :rtype: int
        '''
        return bin(n).count('1')