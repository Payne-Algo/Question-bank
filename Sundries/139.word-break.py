# 139. 单词拆分
'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""

初始化DP：dp，其中dp中都为False。长度为n + 1（左开右闭）
定义dp[0] = True, 当可以被拆分时，第一个词一定为True
tow poniter： i：start j：end
当word[i:j] in wordDict中当时候，则证明可以被拆分
"""




from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # 左开右闭
        dp[0] = True    # 定义初始状态
        # tow pointer: word start -> end
        for i in range(n):  # i:word->start
            for j in range(i + 1, n + 1):  # j: word -> end
                # 如果字符串从第i个字母开始到j字母存在于wordDict
                # 那么可以判断此单词可以被拆分
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


# other Solution
"""
另一种写法：Clear Code
定义dp = True, 当可以被拆分时，第一个词一定为True
循环遍历
基础思路可参考Solution
any关键字
    Return True if bool(x) is True for all values x in the iterable.
    
    If the iterable is empty, return True.
"""


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1, len(s)+1):
            dp += any(dp[j] and s[j:i] in wordDict for j in range(i)),
        return dp[-1]
