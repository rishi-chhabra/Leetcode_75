class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for num in nums[1:]:
            temp = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, max_so_far * num, min_so_far * num)
            max_so_far = temp
            result = max(result, max_so_far)
        return result