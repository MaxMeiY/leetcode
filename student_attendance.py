class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        haha
        """

        count_A = 0
        continums_L = 0
        for i in s:   
            if i == 'A':
                count_A += 1
                if count_A > 1:
                    return False
            if i == 'L':
                continums_L += 1
                if continums_L > 2:
                    return False

            else:
                continums_L = 0
        return True
