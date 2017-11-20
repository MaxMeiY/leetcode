class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
'''
MY Original answer
        if not a:
            return len(b)
        if not b:
            return len(a)
        if a[0] == b[0]:
            return self.findLUSlength(a[1:], b[1:])
        else:
            return max(self.findLUSlength(a[1:],b),
                      self.findLUSlength(a, b[1:]))
'''
        # This is a silly question
        return max(len(a), len(b)) if a != b else -1
