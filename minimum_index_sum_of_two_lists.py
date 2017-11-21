class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        ha
        """
        dict1 = {x:i for i,x in enumerate(list1)}
        dict2 = {x:i for i, x in enumerate(list2)}
        dict3 = {}
        min = float('inf')
        res = []
        for i in dict1.keys():
            if i in dict2:
                dict3[i] = dict1[i] + dict2[i]
                if dict3[i] < min:
                    min = dict3[i]
        for i in dict3.keys():
            if dict3[i] == min:
                res.append(i)
        return res
