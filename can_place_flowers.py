class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False

        i = 0 if flowerbed[0] == 0 else 2
        while i < len(flowerbed):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                i += 2
            elif i == len(flowerbed) -1:
                if flowerbed[i-1] != 1:
                    print(i)
                    n -= 1
                break
            else:
                if flowerbed[i+1] != 1:
                    print(i)
                    n -= 1
                    i += 2
                else:
                    i += 3
        return True if n == 0 else False
    