# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution - 1
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [], []
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            node = stack.pop()
            root = node.left
        return result[::-1]


# Solution - 2

# Solution - 3
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]
