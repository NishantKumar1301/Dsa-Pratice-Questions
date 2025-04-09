class Solution:
    def find_bob_path(self, adj, bob, parent, curr_path, bob_path):
        if bob == 0:
            bob_path[:] = curr_path[:]
            return True
        
        curr_path.append(bob)
        for nbr in adj[bob]:
            if nbr != parent and self.find_bob_path(adj, nbr, bob, curr_path, bob_path):
                return True
        
        curr_path.pop()
        return False

    def find_max_income_for_alice(self, adj, alice, parent, amount):
        max_income = -float('inf')
        
        for nbr in adj[alice]:
            if nbr != parent:
                income = self.find_max_income_for_alice(adj, nbr, alice, amount)
                max_income = max(max_income, income + amount[alice])
        
        return amount[alice] if max_income == -float('inf') else max_income

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        curr_path, bob_path = [], []
        self.find_bob_path(adj, bob, -1, curr_path, bob_path)

        size = len(bob_path)
        for i in range(size // 2):
            amount[bob_path[i]] = 0

        if size % 2 == 1:
            amount[bob_path[size // 2]] = 0
        else:
            amount[bob_path[size // 2]] /= 2 
        
        return self.find_max_income_for_alice(adj, 0, -1, amount)
