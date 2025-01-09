from collections import Counter
from heapq import heapify, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        count = Counter(hand)
        
        # Create a min-heap of unique card values
        mheap = list(count.keys())
        heapify(mheap)
        
        # Process groups from the heap
        while mheap:
            first = mheap[0]  # Get the smallest card
            for i in range(first, first + groupSize):
                if count[i] == 0:  # If a card is missing, return False
                    return False
                count[i] -= 1  # Use one card
                if count[i] == 0:
                    # Remove the card from the heap if its count becomes zero
                    if i != mheap[0]:  # Ensure the heap is in order
                        return False
                    heappop(mheap)
        
        return True
