class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def f(s, delete):
            if len(s) == 0 or len(s) == 1:
                return True
            if s[0] == s[-1]:
                return f(s[1:-1], delete)
            else:
                if delete:
                    return f(s[1:], False) or f(s[:-1], False)
                else:
                    return False
        s_list = list(s)
        return f(s_list, True)

    def ValidPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def take_over(s, i, j, can_delete):
            if can_delete:
                return take_over(s, i+1, j, False) or return take_over(s, i, j-1, False)

            while i < j:
                if s[i] != s[j]:
                    print(s[i], s[j])
                    return False
                i += 1
                j -= 1
            return True

        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            if s[i] != s[j]:
                print('take_over')
                return take_over(s, i, j,True)
                print('never return')
            i += 1
            j -= 1

        return True