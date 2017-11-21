class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        haha
        """
        temp = {chr(x+97) :0 for x in range(26)}
        for i in magazine:
            temp[i] += 1
        for j in ransomNote:
            temp[j] -= 1
            if temp[j] < 0:
                return False
        return True
