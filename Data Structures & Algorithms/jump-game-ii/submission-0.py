class Solution:
    def jump(self, nums: list[int]) -> int:
        count = i = maxReach = pos = 0
        while i < len(nums) - 1:
            maxReach = max(maxReach, i + nums[i])
            if pos == i:
                pos = maxReach
                count += 1
            i += 1
        return count
        