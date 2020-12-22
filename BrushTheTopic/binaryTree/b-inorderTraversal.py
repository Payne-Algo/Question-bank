# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution - 1
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result


# Solution - 2 简化Solution-1
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result

# Solution - 3


class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result
