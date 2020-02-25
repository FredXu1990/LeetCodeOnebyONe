class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
	执行用时 :12 ms
	内存消耗 :12.8 MB
        """
        hashdic = {}

        for i, num in enumerate(nums):
            j = hashdic.get(target - num)
            if j is not None and i != j:
                return [j, i]
            hashdic[num] = i
        return [-1, -1]
