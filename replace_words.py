class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        tre = {}
        END = True
        for root in dict:
            t = tre
            for letter in root:
                if not letter in t:
                    t[letter] = {}
                t = t[letter]
            t[END] = root

        def replace(word):
            t = tre
            for letter in word:
                if not letter in t:
                    break
                t = t[letter]
                if END in t:
                    return t[END]
            return word
        return ' '.join(map(replace, sentence.split()))