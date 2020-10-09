# Violence Time O(n), Memory O(1)
'''
for loop -> i
    for loop -> j 
        if nums[i] + nums[j] == target:
'''
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if  nums[i] + nums[j] == target:
            return i, j

# Otherwise Time O(n), Memory O(1)
# ∵ a + b = target 
# ∴ a = target - b
for i in range(len(nums)):
        a = target - nums[i]
        if a in nums:
            j = nums.index(a)
            if i != j:
                return i, j

# Hash  Time O(n), Memory O(n)
dic = {} # Dictionary
for i in range(len(nums)):
    a = target - nums[i] # 数
    if a in dic:
        return dic[a], i # 数 -> 索引
    dic[nums[i]] = i  # 存入