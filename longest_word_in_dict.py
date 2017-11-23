class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        new_words = sorted(words)
        string = ''
        res = set()
        for i in new_words:
            if len(i) == 1 or i[:-1] in res:
                res.add(i)
                string = i if string == '' else i if len(i) > len(string) else string
        return string
            