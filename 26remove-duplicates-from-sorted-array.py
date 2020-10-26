from typing import List

# part 1 enumeration
# the look is so clear, but it vert slow

def remove_dup(nums: List[int]):
    for i in nums[:]:
        if nums.count(i) > 1:
            nums.remove(i)
        return len(nums)

# part 2:  two pointer:

def remove_duplic(nums:List[int]):
    if len(nums) < 2: return len(nums)
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
