def array_pair_sum(nums):
    '''
    :type nums: List[int]
    :rtype: int
    haha
    '''
    new_nums = sorted(nums, abs)
    print(new_nums)
    result = sum([new_nums[i]
                  for i in range(0, len(nums)-1, 2)])
    return result