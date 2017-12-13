class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapping = {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        # cna't put following two lines into one, such as
        # temp = [(..)].sort(..)
        # cause sort() will return None!!!!!
        # be careful!
        temp = [(i,mapping[i]) for i in mapping]
        temp.sort(key=lambda x:x[1], reverse=True)
        return ''.join(item[0]*item[1] for item in temp)
