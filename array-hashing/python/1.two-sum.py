class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}

        for i, num in enumerate(nums):
            want = target - num
            if want in targetDict:
                return [targetDict[want], i]

            targetDict[num] = i