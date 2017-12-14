class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.dict[len(i)] = self.dict.get(len(i), [])
            self.dict[len(i)].append(i)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
       # print(self.dict)
        for i in self.dict.get(len(word), []):
            count_diff = 0
            for j in range(len(i)):
                if i[j] != word[j]:
                    count_diff += 1
            if count_diff == 1:
                return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)