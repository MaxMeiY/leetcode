class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        new_nums1 = sorted(nums1)
        new_nums2 = sorted(nums2)
        i = 0
        j = 0
        len1 = len(new_nums1)
        len2 = len(new_nums2)
        while i < len1 and j < len2:
            if new_nums1[i] == new_nums2[j]:
                res.append(new_nums1[i])
                i += 1
                j += 1
            elif new_nums1[i] < new_nums2[j]:
                i += 1
            else:
                j += 1

        return res