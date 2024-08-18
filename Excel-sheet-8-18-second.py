class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""  #初始化一个空字符串，用来存储转换后的标题
        while n:  #使用一个循环来处理数字n，直到n 变为0
            n, y = divmod(n, 26)#使用divmod获取商n和余数y,这里n时除以26的商，y是除以26后的余数
            if y == 0:# 如果余数y等于0，说明n是26的倍数，
                n -= 1 #将商n-1，因为在Excel列标题没有以0结尾的
                y = 26 #将余数y设置为26，因为在Excel中，每26个字母循环一次
            res = chr(y + 64) + res#将余数y加上64(ASCll码中A的值是65，)然后使用chr函数转换成对应的大写字母，并将其添加到结果字符串res的前面
        return res#返回转换后的Excel列标题字符串