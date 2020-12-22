# DFS | BFS 

## 搜索｜遍历

- 每个节点访问一次
- 每个及节点且仅遍历一次
- 对于搜索的顺序不同
  - 深度优先(DFS)
  - 广度优先(BFS)
  - 优先级搜索

### DFS

```python
# Recursive
visited = set() 
def dfs(node):
  if node in visited:
    # already visited
    return 
  visited.add(node)
  # process current node
  # logic here
  dfs(node.left)
  dfs(node.right)
  
# 如果是多叉树
visited = set()
def dfs(node):
  visited.add(node)
  for next_node in node.children():
      if not next_node in visited:
    		dfs(next,visited)
        
# Iterative
#Python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...

```
### BFS

```python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
    
```



