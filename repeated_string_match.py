class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B) / len(A))
        return times * (B in A*times) or (times+1) * (B in A*(times+1)) or -1