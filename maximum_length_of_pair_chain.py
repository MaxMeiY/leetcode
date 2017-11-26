class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        haha
        """
        if pairs == []:
            return 0
        pairs.sort(key=lambda a: a[1])
        length = 1
        start = pairs[0]
        for i in range(1,len(pairs)):
            if start[1] < pairs[i][0]:
                length += 1
                start = pairs[i]
        return length
