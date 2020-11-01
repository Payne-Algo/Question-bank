# 二叉树 Binary tree
# 前 中 后 Front, middle and back
# Definition for a binary tree node.
from typing import List

# Python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)

        res = list()
        helper(root)
        return res

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root: TreeNode):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        res = list()
        helper(root)
        return res

# golang
# /**
#  * Definition for a binary tree node.
#  * type TreeNode struct {
#  *     Val int
#  *     Left *TreeNode
#  *     Right *TreeNode
#  * }
#  */
func preorderTraversal(root *TreeNode) (vals []int) {
    var preorder func(*TreeNode)
    preorder = func (node *TreeNode) {
        if node == nil {return}
        vals = append(vals, node.Val)
        preorder(node.Left)
        preorder(node.Right)
    }
    preorder(root)
    return
}

func inorderTraversal(root *TreeNode) []int {
	ret := []int{}
	st(root, &ret)
	return ret
}

func st(root *TreeNode, ret *[]int) {
	if root == nil {return}
	st(root.Left, ret)
	*ret = append(*ret, root.Val)
	st(root.Right, ret)
}

