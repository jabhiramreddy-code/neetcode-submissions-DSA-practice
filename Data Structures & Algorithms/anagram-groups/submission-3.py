class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        for i in strs:
            sort = tuple(sorted(i))
            if sort not in maps:
                maps[sort] = []
            maps[sort].append(i)

        return list(maps.values())
