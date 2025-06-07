from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)
        email_to_name = {}
        
        # Build adjacency list and map email to name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                adj_list[first_email].append(email)
                adj_list[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        merged_accounts = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in adj_list[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for account in accounts:
            email = account[1]
            if email not in visited:
                component = []
                dfs(email, component)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts
