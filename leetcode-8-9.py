class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = list() #初始化一个列表ret,用于存储所有满足条件的路径；
        path = list() # 初始化一个列表path,用于存储当前递归路径上的节点值；

        def dfs(root: TreeNode, targetSum: int): 
            #定义了一个辅助函数，接受当前节点root和剩余目标和targrtSum;
            if not root:
                return 
            path.append(root.val) #将根结点的值添加到path中；
            targetSum -= root.val  #从剩余目标和中减去当前结点的值；
            if not root.left and not root.right and targetSum == 0:
            #如果当前节点是叶子节点(没有左右节点),并且剩余目标和为0，说明找到一条满足条件的路径；
                ret.append(path[:]) #将当前条件的路径的副本添加到ret当中；
            dfs(root.left, targetSum)#递归调用dfs函数，遍历左子树
            dfs(root.right, targetSum)#遍历右子树
            path.pop()#回溯步骤，从当前列表路径path中一处最后一个节点的值；

        dfs(root, targetSum)#从根节点开始递归，初始化目标和为targetSum
        return ret
            