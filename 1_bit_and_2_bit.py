class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        haha
        """
        index = 0
        while index < len(bits):
            print(index)
            if index == len(bits) -1:
                return True
            if index == len(bits) - 2:
                if bits[index] == 1:
                    return False
                else:
                    return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1