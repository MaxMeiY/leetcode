class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        temp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        # initilize the table
        for i in range(1, len(s1)+1):
            temp[i][0] = temp[i-1][0] + ord(s1[i-1])
        for j in range(1, len(s2)+1):
            temp[0][j] = temp[0][j-1] + ord(s2[j-1])

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    temp[i][j] = temp[i-1][j-1]
                else:
                    temp[i][j] = min(
                        temp[i-1][j]+ord(s1[i-1]),
                        temp[i][j-1]+ord(s2[j-1]))
        return temp[len(s1)][len(s2)]