# Wrong Answer
'''class Solution:
    def countBinarySubstrings(self, s):

        :type s: str
        :rtype: int




        result = 0
        for step in range(2, len(s)+1, 2):
            for i in range(0, len(s)-step+1):

                start = i
                print('--------', start)
                print(start)
                end = start + step
                n_of_0 = s[start:end].count('0')
                n_of_1 = s[start:end].count('1')
                group_together = True
                if s[start:step].count('0') != 0 and \
                   s[start:step].count('1') != 0:
                    group_together = False
                if s[step:end].count('0') != 0 and \
                   s[step:end].count('1') != 0:
                    group_together = False
                print(group_together, s[start:end])
                if n_of_0 == n_of_1 and group_together:
                    result += 1

                print('----------')

        return result
'''

# Awsome Awsome!!!!!!
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_run_len = 0
        cur_run_len = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_run_len += 1
            else:
                pre_run_len = cur_run_len
                cur_run_len = 1

            if pre_run_len >= cur_run_len:
                res += 1
        return res
