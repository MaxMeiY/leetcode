class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse_k(a_list, start, k):
            while start < k:
                a_list[start], a_list[k-1] = a_list[k-1], a_list[start]
                start += 1
                k -= 1
        a_list = list(s)
        i = 0
        length = len(a_list)
        while i < length:
            if length - i < k:
                reverse_k(a_list, i, length)
                break
            elif length - i < 2 *k and length - i >= k:
                reverse_k(a_list, i, i+k)
                break
            else:
                reverse_k(a_list, i, i+k)
                i += 2 * k
        return ''.join(a_list)


    def f(self, s, k):
        i = 0
        while i < len(s):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
            i += 2 * k
        return s