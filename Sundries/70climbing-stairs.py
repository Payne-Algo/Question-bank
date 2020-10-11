
'''
f(1) = 1
f(2) = 2
f(3) = 3
f(4) = F(n - 1) + F(n - 2) 
'''
# recursion Time O(2 ^ n), Memory O(1)
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        else: return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# recursion + memo Time O(n ^ 2), Memory O(n)
class Solution2:
    @functools.lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        else: return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Array Dynamic recursion Time O(n) memory O(n)

class Solution3:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)] # new List
        dp[0], dp[1] = 1, 1 # set Initial value
        for i in range(2, n + 1): 
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# three pointers to Simple dynamic recursion
class Solution4:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        i, j, k = 0, 0, 1
        for i in range(n):
            i = j
            j = k
            k = i + j
        return k

# two Sum pointers Simple dynamic recursion  Time O(n), Memory O(1)
class Solution5:
    def climbStairs(self, n: int) -> int:
    now, next = 0, 1
            for _ in range(n + 1):
                now, next = next, now + next
            return now

# Math Time O(1), Memory O(1)
class Solution6:
    def climbStairs(self, n: int) -> int:
        from math import pow
        sqrt5 = 5 ** 0.5
        func = pow((sqrt5 + 1) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)
        return int(func / sqrt5)