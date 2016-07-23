class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permuteHelper(nums, res, 0)
        return res

    def permuteHelper(self, nums, res, start):
        if start == len(nums) - 1:
            res.append(list(nums))
            return
        for i in range(start, len(nums)):
            if self.isSwap(nums, start, i):
                nums[start], nums[i] = nums[i], nums[start]
                self.permuteHelper(nums, res, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    def isSwap(self, nums, start, end):
        for i in range(start, end):
            if nums[i] == nums[end]:
                return False
        return True
