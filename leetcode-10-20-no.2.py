class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i 
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i,j))
            i = j + 1
        return ans
    #假设：
    #nums = [1,2,3,5,6,7,9]
    # i = j = 1
    # j+1=2 < len(nums),2 < 6 and nums[1+1] == nums[1]+1

