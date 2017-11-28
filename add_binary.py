class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec_a = int(a, 2)
        dec_b = int(b, 2)
        return format(dec_a+dec_b, 'b')
        