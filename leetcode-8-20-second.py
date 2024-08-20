class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        # 生成一个由 0 ——31 的数字序列。
        # 对于序列中的每个数字i,检查n的第i位(从0开始计数)是否为1.
        # 是将数字1左移i位。
        # 最后是一个位于操作，如果n的第i位是1，否则是0.
        # 将所有为1的结果加起来，得到汉明重量。
        return ret