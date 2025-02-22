class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        word = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            # Using set membership is O(1)
            while left < right and word[left] not in vowels:
                left += 1
            while left < right and word[right] not in vowels:
                right -= 1
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return ''.join(word)