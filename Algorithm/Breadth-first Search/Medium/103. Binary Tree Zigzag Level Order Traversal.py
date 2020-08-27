'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

Solution:

# BFS 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level_list = deque()
        
        # check edge case
        if root is None:
            return []
        
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True
        
        while len(node_queue) > 0 :
            curr_node = node_queue.popleft()
            
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
                    
            else:
                # we finish one level
                res.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)
                
                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left
        return res
            
