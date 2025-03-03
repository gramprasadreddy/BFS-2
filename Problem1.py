# Problem 1 : Binary Tree Right Side View
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

from collections import deque
# Your code here along with comments explaining your approach
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # initialize the result 
        right_side_view = []

        #if the tree is empty return the result
        if root is None:
            return right_side_view
        
        # Use deque to hold the nodes for doing bfs traversal
        queue = deque([root])

        # loop till queue is not empty
        while (queue):
            # get the size of the queue at a particular level
            size = len(queue)
            for i in range(size):
                # pop the top element from the queue
                current_node = queue.popleft()
                # Check if the element is last element for the particular level
                if (i == size-1):
                    right_side_view.append(current_node.val)
                
                # If the node has left child then add to queue
                if current_node.left:
                    queue.append(current_node.left)
                
                # If the node has right child then add to queue
                if current_node.right:
                    queue.append(current_node.right)

        return right_side_view
        