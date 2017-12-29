class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        My slow solution.
        first thought
        """
        ans = float('inf')
        for row in wall:
            prev = 0
            for i in range(0, len(row)-1):
                res = 0
                edge = row[i] + prev
                for r in wall:
                    s = 0
                    for j in range(0, len(r)):
                        if edge == s + r[j]:
                            break
                        elif edge > s+r[j]:
                            s = s + r[j]
                        else:
                            res += 1
                            break
                prev += row[i]
                if res < ans:
                    ans = res
        return ans if ans != float('inf') else len(wall)

if __name__ == '__main__':
    a = [[1,2,2,1],
         [3,1,2],
         [1,3,2],
         [2,4],
         [3,1,2],
         [1,3,1,1]]
# easy solution
# collections.defaultdict
# python3 d.values() not a list, but in python3 it's a list.
    def f(wall):
        import collections
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        print(len(wall) - max(list(d.values()) + [0]))
    f(a)