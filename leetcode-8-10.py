class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 初始化当前行
        res = [1] * (rowIndex + 1)  #初始化列表
        for i in range(2, rowIndex + 1):#从第三行开始遍历直到倒数第一个元素
            for j in range(i - 1, 0,-1):#逆序遍历，从当前行的倒数第二个元素开始遍历
                res[j] += res[j - 1]# 
        return res