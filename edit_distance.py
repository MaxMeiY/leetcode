class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        table = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        # initilize table
        for i in range(1, len(word1)+1):
            table[i][0] = i

        for j in range(1, len(word2)+1):
            table[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(
                        1 + table[i-1][j], #Delete
                        1 + table[i-1][j-1], # Replace
                        1 + table[i][j-1] # Insert
                    )
        return table[len(word1)][len(word2)]