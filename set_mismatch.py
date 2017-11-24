class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_map = [0 for i in range(len(nums))]
        for i in nums:
            num_map[i-1] += 1
        for i in range(len(num_map)):
            if num_map[i] == 0:
                loss = i+1
            elif num_map[i] == 2:
                twice = i+1
        print(loss, twice)
        return [twice, loss]
    