class Solution:

    def __init__(self, nums: List[int]):
        self.index_hash = defaultdict(list)
        for i in range(len(nums)):
            self.index_hash[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_hash[target])