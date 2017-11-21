class Solution:
    import math
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        haha
        """
        for width in range(int(math.sqrt(area)), 0, -1):
            if width * (area // width) == area:
                return [area//width, width]
