from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        q = deque()
        res = []

        # Build adjacency list and indegrees array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1  # Indegree is updated while processing the prerequisites

        # Add courses with no prerequisites to the queue
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        # Process the graph using BFS
        while q:
            course = q.popleft()
            res.append(course)

            # Decrease indegree for neighboring courses and add to queue if indegree becomes 0
            for neighbor in adj[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        # If the result contains all courses, return the order; otherwise, return an empty list (cycle detected)
        return res if len(res) == numCourses else []

