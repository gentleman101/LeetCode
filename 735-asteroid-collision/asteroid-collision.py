from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while asteroid < 0 and stack and stack[-1] > 0:
                # Handle collision
                if abs(asteroid) > stack[-1]:  # Current asteroid destroys the top of the stack
                    stack.pop()
                elif abs(asteroid) == stack[-1]:  # Both asteroids destroy each other
                    stack.pop()
                    break
                else:  # Top of the stack destroys the current asteroid
                    break
            else:
                # If no collision occurs, add the asteroid to the stack
                stack.append(asteroid)

        return stack
