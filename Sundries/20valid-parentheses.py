#
# 定义范围
def vaild(s):
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []  # 创建栈
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack
