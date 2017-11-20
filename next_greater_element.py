class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        haha
        """
        result = []
        for num in nums1:
            index = 0
            next_greater = None
            while index < len(nums2):
                if num == nums2[index]:
                    break
                index += 1
            found = False
            for i in range(index, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result