class Solution:
    def isHappy(self, n: int) -> bool:
        a = []  #初始化一个空列表a,用于存储在计算过程中遇到的所有数，已检测循环；
        s = 0  #初始化一个变量s，用于存储每一位数字的平方和；
        while(True):  #开始一个无限循环，这个循环会一直执行，直到满足某个条件并退出；
            for i in str(n):  #将整个n转换位字符串，然后遍历字符串中的每一个字符(即n的每一位数字)
                s += int(i) ** 2  #将当前遍历到的数字转换为整数，并计算其平方，然后加到变量s上；
            n = s  #将计算出的平方和赋值给n，准备进行下一轮的计算；
            s = 0  #重置变量s为0，为下一轮计算做准备；
            if(n == 1):  # 如果n等于1,说明已经达到了快乐数的重点；
                return True
            if n in a:  # 如果n已经在列表a中出现过，说明已经形成了循环，返回False.
                return False
            a.append(n)  #  将当前n添加到列表a中，用于记录已经计算过的数；