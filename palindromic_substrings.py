class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return 0
        ans = len(s)
        for sub_len in range(2, len(s)+1):
            for start in range(0, len(s)-sub_len+1):
                end = start + sub_len - 1
                if self.helper(s, start, end):
                    ans += 1

        return ans

    def helper(self, string, start, end):
        if start >= end:
            return True
        if string[start] != string[end]:
            return False
        return self.helper(string, start+1, end-1)


    def DP_countSubstrings(self, s):
        if len(s) <= 0:
            return 0

        res = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            res[i][i] = 1

        for sub_len in range(2, len(s)+1):
            for start in range(0, len(s)-sub_len+1):
                end = start + sub_len - 1
                if start + 1 > end - 1:
                    if s[start] == s[end]:
                        res[start][end] = 1
                else:
                    if res[start+1][end-1] == 1 and s[start] == s[end]:
                        res[start][end] = 1

        return sum(sum(i) for i in res)


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings('aaa'*30))
    print(s.DP_countSubstrings('aaa'*30))