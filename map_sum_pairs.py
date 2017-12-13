class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.mapping[key] = val
        return None
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ans = 0
        l_prefix = len(prefix)
        for key in self.mapping:
            if prefix == key[:l_prefix]:
                ans += self.mapping[key]
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)