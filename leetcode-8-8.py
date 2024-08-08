class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = inf  
#定义ans并且初始化无穷大(inf)
        def dfs(node:Optional[TreeNode], cnt: int) ->None: 
#定义了一个辅助函数，接受两个参数，node是当前节点，cnt是从根节点到当前结点的路径长度
            if node is None:
                return
            cnt += 1
            if node.left is node.right:  
#检查当前节点是否是叶子节点，即没有子节点
                nonlocal ans  
#声明ans为非全局变量,允许在dfs函数内部修改ans变量的值
                ans = min(ans, cnt)
#使用min函数更新ans的值，如果cnt小于当前的ans，则将ans更新为cnt的值
                return
            dfs(node.left, cnt)#递归调用,遍历左子树
            dfs(node. right, cnt)#递归调用，遍历右子树
        dfs(root, 0)    #从根节点开始，初始化路径长度为0，调用dfs函数
        return ans if root else 0
        #如果根节点root不是None,则返回ans的值,反之返回0，表示深度为0