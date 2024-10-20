class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        left = self.invertTree(root.left) #利用inverTree方法传入左子树，并反转，赋给left变量
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root 
