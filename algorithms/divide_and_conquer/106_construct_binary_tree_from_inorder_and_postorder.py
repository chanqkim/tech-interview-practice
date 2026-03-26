'''
link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-divide-and-conquer

Key Logic Breakdown
To understand why this works, remember these two rules:

Post-order (Left → Right → Root): The last element is always the Root.

In-order (Left → Root → Right): Once you find the Root, everything to its left belongs to the Left Subtree, and everything to its right belongs to the Right Subtree.

Slicing inorder[:idx]: We take all elements to the left of the root found in the in-order array.

Slicing postorder[:idx]: Since the number of nodes in the left subtree is the same regardless of the traversal method, we take the first idx elements from the post-order array to build that same left subtree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# time: O(n^2) space: O(n)
# time analysis: finding the index of the root value in the inorder array takes O(n) time, and this is done for each node in the tree, resulting in O(n^2) time complexity
# space analysis: the maximum depth of the recursion is O(n) in the worst case (when the tree is skewed), and we also store the tree nodes in memory, resulting in O(n) space complexity
class Solution:
    def buildTree(self, inorder, postorder):
        # 1. Base case: If the inorder list is empty, there are no nodes to process.
        if not inorder:
            return None

        # 2. The last element of postorder is always the root of the current (sub)tree.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 3. Find the index of the root in the inorder list.
        # This divides the tree into Left and Right subtrees.
        idx = inorder.index(root_val)

        # 4. Recursively build the Left subtree.
        # Inorder: elements before the root index.
        # Postorder: first 'idx' elements (matching the size of the left subtree).
        root.left = self.buildTree(inorder[:idx], postorder[:idx])

        # 5. Recursively build the Right subtree.
        # Inorder: elements after the root index.
        # Postorder: elements from 'idx' up to (but not including) the last root.
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        # 6. Return the constructed root node.
        return root