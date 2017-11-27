class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0 or mapping[stack.pop()] != i:
                    return False
            print(stack)
        return True if len(stack) == 0 else False
