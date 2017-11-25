class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        i = 0
        while i < len(chars):
            start, start_index = chars[i], i
            length = 1
            while i+1 < len(chars) and chars[i+1] == start:
                length += 1
                i += 1
            if length >1:
                chars[start_index+1:start_index+length] = str(length)
            i = start_index+2 if length > 1 else start_index + 1
        return len(chars)
    