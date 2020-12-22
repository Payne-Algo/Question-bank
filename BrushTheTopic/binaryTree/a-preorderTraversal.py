# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution-1
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [], []
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return result


# Solution-2	简化Solution-1
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return result


# Solution-3
class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
