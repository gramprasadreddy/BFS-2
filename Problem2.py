# Problem 2 : Cousins in Binary Tree
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # if the tree is empty return False
        if root is None:
            return False

        # Initialize the queue for storing the root and its parent for bfs traversal
        queue = deque([(root, None)])

        # loop unitl till queue is not empty
        while (queue):
            # size of the level
            level_size = len(queue)
            # boolean variable to check if x and y is found or not
            x_found = False
            y_found = False
            # traversing all the nodes at a particular level
            for _ in range(level_size):
                # poping the first element and its parent from the queue
                curr_node, parent = queue.popleft()
                # with x and y setting the variable accordingly
                if curr_node.val == x:
                    x_found = True
                    x_parent = parent
                if curr_node.val == y:
                    y_found = True
                    y_parent = parent
                # If the node has left child then add to queue
                if curr_node.left:
                    queue.append((curr_node.left, curr_node))
                # If the node has right child then add to queue
                if curr_node.right:
                    queue.append((curr_node.right, curr_node))
            
            # checking if the x and y is found or not. 
            # if they are found then checking their parent. If they are not same then return True else return False
            if x_found and y_found:
                return x_parent != y_parent
            # return false if one of them is found
            elif x_found or y_found:
                return False
        return False

        