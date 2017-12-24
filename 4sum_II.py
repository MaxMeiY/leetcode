class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        temp = {}
        for a in A:
            for b in B:
                half = a + b
                if half in temp:
                    temp[half] += 1
                else:
                    temp[half] = 1

        for c in C:
            for d in D:
                other_half = 0 - (c + d)
                if other_half in temp:
                    ans += temp[other_half]
        return ans

    '''
    consice solution
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
    '''