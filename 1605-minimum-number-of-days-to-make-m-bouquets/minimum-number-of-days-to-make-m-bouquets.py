class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(days: int) -> bool:
            bouquets, flowers = 0, 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:  # Early exit if enough bouquets are made
                    return True
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                answer = mid  # Update the result and search for fewer days
                right = mid - 1
            else:
                left = mid + 1

        return answer
