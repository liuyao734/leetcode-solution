class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0    #初始化变量ret，用来存储最终的结果
        for i in columnTitle:  #遍历每个字母
            ret = ret * 26 + ord(i) - 64
            #使用ord(i)获取对应ASCII码然后减去64，并将ret乘以 26，因为每个字母可能是1——26个字母的任意一个数字
        return ret