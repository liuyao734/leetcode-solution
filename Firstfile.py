from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
        nums = [2, 7, 11, 15]  
        target = 9  
        solution = Solution()  
        print(solution.twoSum(nums, target))  # 应该输出 [0, 1]，因为 2 + 7 = 9