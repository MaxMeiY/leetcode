class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        good ieda; but I didn't think of it.
        """
        res = 0
        for i in points:
            cmap = {}
            for j in points:
                x = j[0] - i[0]
                y = j[1] -i[1]
                cmap[x*x + y*y] = 1 + cmap.get(x*x+y*y, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k]-1)
        return res