class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        haha
        """
        if r * c != len(nums[0]) * len(nums):
            return nums
        result = []
        for row in nums:
            for row_item in row:
                result.append(row_item)

        new_matrix = []
        index = 0
        for i in range(r):
            row_of_matrix = []
            for j in range(c):
                row_of_matrix.append(result[index])
                index += 1
            new_matrix.append(row_of_matrix)
        return new_matrix