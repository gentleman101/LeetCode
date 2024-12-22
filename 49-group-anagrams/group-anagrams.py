from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)  # Use defaultdict to simplify appending

        for i in strs:
            key = tuple(sorted(i))  
            anaDict[key].append(i)

        return list(anaDict.values())
