class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        prefix_sum[0] = 1
        run_sum = 0
        cnt = 0
        for num in nums:
            run_sum+=num
            target = run_sum-k
            
            if prefix_sum.get(target,0)>0:
                cnt+=prefix_sum[target]

            prefix_sum[run_sum] = prefix_sum.get(run_sum, 0) + 1


        return cnt
           
