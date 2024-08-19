class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        #创建计数器对象，nums是一个列表，Counter会遍历整个列表
        return max(counts.keys(), key = counts.get)
        #返回Counter键所有的值，返回的是出现次数最多的元素。