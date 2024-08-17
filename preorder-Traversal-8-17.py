class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root: TreeNode):
            if not root:#如果root为空，则递归结束
                return
            res.append(root.val) #将当前节点值root.val添加到结果列表res中
            preorder(root.left)# 递归调用preorder函数，遍历当前结点的右子树
            preorder(root.right)# 上同
        res = list()  #初始化一个空列表res，用来存储前序遍历结果
        preorder(root) #调用辅助函数，从根节点开始遍历
        return res  #返回存储前序遍历结果的列表