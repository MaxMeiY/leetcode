class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = {}
        for i in range(len(nums)):
            if not nums[i] in mapping:
                mapping[nums[i]] = i
            else:
                if abs(mapping[nums[i]] - i) <= k:
                    return True
                mapping[nums[i]] = i
        return False
