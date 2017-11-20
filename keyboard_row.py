class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        haha
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        result = []
        for y in words:
            contain = True
            x = y.lower()

            if x[0] in row1:
                in_row = 'row1'
            if x[0] in row2:
                in_row = 'row2'
            if x[0] in row3:
                in_row = 'row3'

            for char in x:
                if char in row1:
                    if in_row != 'row1':
                        contain = False
                if char in row2:
                    if in_row != 'row2':
                        contain = False
                if char in row3:
                    if in_row != 'row3':
                        contain = False
            if contain:
                result.append(y)
        return result