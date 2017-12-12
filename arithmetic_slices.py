'''
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        if len(A) < 3:
            return 0

        for step in range(3, len(A)+1):
            for start in range(0, len(A)-step+1):
                end = start + step
                diff = A[start+1] - A[start]

                for i in range(start+1, end):

                    if A[i] - A[i-1] != diff:
                        break
                    elif i == end-1:
                        count += 1
        return count
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        if len(A) < 3:
            return 0

        count = 0
        prev = 0
        diffs = [A[i] - A[i-1] for i in range(1, len(A))]
        for i in range(1, len(diffs)):
            if diffs[i] == diffs[i-1]:
                count = count + 1
                prev = count + prev
            else:
                count = 0
        return prev




if __name__ == '__main__':
    s = Solution()
    sample = [1,2,3,8,9,10]
    print(s.numberOfArithmeticSlices(sample))