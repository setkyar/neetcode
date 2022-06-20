# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Time:
# O(nlogn)
# Space:
# O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False

# Time:
# O(n)
# Space:
# O(n)
class SolutionOne:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        hashset = set()

        for i in nums:
            if i in hashset:
                return True

            hashset.add(i)

        return False