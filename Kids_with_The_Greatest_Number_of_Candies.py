class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

        # Alternative implementation using a loop:
        # result = []
        # for candy in candies:
        #     result.append(candy + extraCandies >= max_candies)
        # return result