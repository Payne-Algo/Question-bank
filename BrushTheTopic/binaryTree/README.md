## Brush the topic-BinaryTree

大家好，这是Brush the topic的第一章节,BinaryTree。首先我说一下为什么把这个放在刷题的第一节呢？

原因如下:

- 培养、训练自己的计算机的思维。
- 锻炼模版化，抽象化思维

下面让我们一起去完成一个壮举，那就是完全解决二叉树的遍历问题，以及相关问题。are you ok？

### 知识点回顾

#### 二叉树的遍历

由于对于二叉树的遍历顺序不同，构造出三种不同的遍历方式

- 前序遍历-根左右
- 中序遍历-左根右
- 后序遍历-左右根

#### 递归代码模版如下

**Python**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历
def preOreder(self, root):
  if root:
    self.traverse_path.append(root.val)
    preOreder(self.left)
    preOreder(self.right)

# 中序遍历
def inOreder(self, root):
  if root:
    preOreder(self.left)
    self.traverse_path.append(root.val)
    preOreder(self.right)
    
# 后序遍历
def postOreder(self, root):
  if root:
    preOreder(self.left)
    preOreder(self.right)
    self.traverse_path.append(root.val)
```

**Golang**

```go
// 前序遍历
func preOreder(root *TreeNode) {
  result := []int{}
  if root == nil {return}
  result  = append(result, root.value)
  preOreder(root.Left)
  preOreder(root.Right)
}

// 中序遍历
func inOreder(root *TreeNode) {
  result := []int{}
  if root == nil {return}
  preOreder(root.Left)
  result  = append(result, root.value)
  preOreder(root.Right)
}

    
// 后序遍历
func postOreder(root *TreeNode) {
  result := []int{}
  if root == nil {return}
  postOreder(root.Left)
  postOreder(root.Right)
  result  = append(result, root.value)
}
```

### practice

基于此我们可以拿下以下题目,完全二叉树递归模版解题

### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)-Python

#### **Recursive**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive-1 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None: return
        result.append(root.val)
        self.helper(root.left,result)
        self.helper(root.right, result)
# Recursive-2 Another way Anonymous function
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if not root: return 
            res.append(root.val)
            helper(root.left)
            helper(root.right)
            
        res = list()
        helper(root)
        return res

# Recursive-3 more clean code
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        res.append(root.val)
        res+=self.preorderTraversal(root.left)
        res+=self.preorderTraversal(root.right)
        return res
```

#### **Iterative**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution-1
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
         stack, result = [], []
         while stack or root:
             while root:
                 # 前序遍历-根左右，先拿根
                 result.append(root.val)
                 # 压栈
                 stack.append(root)
                 # 拿完根之后拿左儿子
                 root = root.left
             # 左儿子拿出来，拿右儿子
             node = stack.pop()
             root = node.right
        # # 完成
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
        stack, result = [root], []
        while stack:
            # 拿出根
            node = stack.pop()
            if node:
                # 前序遍历拿出，先拿根的值                
                result.append(node.val)
                # 模仿栈，先入后出。后拿右孩子
                stack.append(node.right)
                stack.append(node.left)
        return result
```

### [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)-Python

#### **Recursive**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive-1 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None: return
        self.helper(root.left,result)
        result.append(root.val)
        self.helper(root.right, result)
        
# Recursive-2 Another way Anonymous function
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if not root: return 
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        res = list()
        helper(root)
        return res

# Recursive-3 more clean code
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        res+=self.preorderTraversal(root.left)
        res.append(root.val)
        res+=self.preorderTraversal(root.right)
        return res
```

#### **Iterative**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution - 1
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return 
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
class Solution:
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
```

### [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

#### **Recursive**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive-1 
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None: return
        self.helper(root.left,result)
        self.helper(root.right, result)
        result.append(root.val)
        
# Recursive-2 Another way Anonymous function
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if not root: return 
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        res = list()
        helper(root)
        return res

# Recursive-3 more clean code
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        res+=self.preorderTraversal(root.left)
        res+=self.preorderTraversal(root.right)
        res.append(root.val)
        return res
```

#### **Iterative**

```python
# Solution - 1
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
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
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return result[::-1]
      
# Solution - 3
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
      	if not root: return
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]
```

二叉树迭代遍历模版-Python

```python
# 前序遍历
# Solution-1
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        stack, result = [], []
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return result
       
# 中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return 
        stack, result = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result
```

由递归到迭代，基本的思想就是由递归中由系统维护的栈，转为手动维护。

