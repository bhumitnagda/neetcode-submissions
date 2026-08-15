class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for string in strs:
            sort_string = ''.join(sorted(string))
            if sort_string not in strings:
                strings[sort_string] = []
            strings[sort_string].append(string)
        return list(strings.values())