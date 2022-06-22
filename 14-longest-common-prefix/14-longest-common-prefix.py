class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if ch != other[i]:
                    return shortest[:i]

        return shortest