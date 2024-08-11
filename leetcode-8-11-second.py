#回文串概念：
#1.所有大写字符转换为小写字符;
#2.移除所有非字母数字字符之后;
#3.短语正着读和反着读都一样;   --><回文串！>
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left,right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True