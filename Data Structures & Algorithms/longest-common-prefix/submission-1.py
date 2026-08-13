class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = min(strs,key=len)
        for i in range(len(first_str)):
            for j in strs:
                if j[i] != first_str[i]:
                    return first_str[:i]
        return first_str

