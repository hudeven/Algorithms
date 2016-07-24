class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = sum = -(1 << 31)
        for n in nums:
            sum = sum + n if sum > 0 else n
            max = sum if sum > max else max
        return max
