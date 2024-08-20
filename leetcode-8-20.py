class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0  #初始化一个变量ret，用于存储反向排列后的结果
        for i in range(32):   #使用一个循环，从0到31遍历32次，对应32位整数的每一位
            ret = (ret <<1) + (n & 1)   #将ret左移一位/就算n的最低位
            n >>= 1   #将n右移一位，丢弃原来的最低位，准备处理下一位
        return ret
        