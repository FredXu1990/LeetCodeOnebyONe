class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i, j = 0, 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j:
        #             nums[i] = 0
        #         j += 1
        # zero = 0 #position of zero
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero += 1
        count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums += [0] * count