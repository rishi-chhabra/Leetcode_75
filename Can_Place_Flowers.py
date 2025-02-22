class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    # Add 0 at start and end to handle edge cases
        flowerbed = [0] + flowerbed + [0]
        count = 0
    
    # Check each position from index 1 to len-2
        for i in range(1, len(flowerbed)-1):
        # If current position and adjacent positions are empty
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
              flowerbed[i] = 1 
              count += 1
    
        return count >= n
