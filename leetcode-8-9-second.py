class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1] * (i + 1) for i in range(numRows)]
        #初始化一个杨辉列表
        #当 numRows = 4时：
        #c[0] = 1 * (0 + 1);
        #c[1] = 1 * (1 + 1);
        #       …………
        for i in range(2, numRows):#遍历第二行的元素，因为第一行和第二行已经初始化；
            for j in range(1, i): #遍历每一行的元素，除了第一个和最后一个元素
                #左上方的数 + 正上方的数
                c[i][j] = c[i - 1] [j - 1] + c[i - 1][j]
                #c[2][1] = c[2-1][0] + c[2-1][1]
        return c