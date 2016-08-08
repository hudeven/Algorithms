class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = reduce(lambda x,y : x+y, nums)
        multiply = len(nums) * (len(nums) + 1) / 2
        return multiply - sum
