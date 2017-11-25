class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        i = 0
        j = len(s)-1
        temp = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while i != j:
            while i< j and not temp[i] in vowels:
                i += 1
            while i < j and not temp[j] in vowels:
                j -= 1
            if i >= j:
                break
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
            j -= 1
        return ''.join(temp)
