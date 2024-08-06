class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            def recur(L, R):
                if not L and not R:
                    return True
                if not L or not R or L.val != R.val:
                    return False
                return recur(L.left, R.right) and recur(L.right, R.left)
            return not root or recur(root.left, root.right)