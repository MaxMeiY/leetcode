class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        temp_heat = sorted(heaters) + float('inf')
        r = i = 0
        for x in sorted(houses):
            while x > temp_heat[i:i+2] / 2:
                i += 1
            r = max(r, abs(temp_heat[i] - x))
        return r