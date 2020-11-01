# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# part 1 two dic
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

# part 2 once dic
#
# 使用中间容器dic，a与b比较， 一个放入，一个取出
# Using the intermediate container DIC, a and B are compared
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False
        for value in dic.values():
            if value != 0:
                return False

# part3: sorted 之后比较。
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)