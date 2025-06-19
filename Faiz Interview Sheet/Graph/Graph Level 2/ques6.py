#Question : Dijkstra?
#Link to the question:  https://codeforces.com/contest/20/problem/C

from heapq import heappush,heappop
n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
dist= [float('inf')]*(n+1)
parent = [-1]*(n+1)
for i in range(1,n+1):
    parent[i]=i
dist[1]=0
for _ in range(m):
    u,v,w = map(int,input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))

pq = [(0,1)] #(dist,node) src = 1 at distance of 0 
while pq:
    dis, node = heappop(pq)
    for item in adj[node]:
        adjNode = item[0]
        edgeWeight = item[1]
        if edgeWeight+dis<dist[adjNode]:
            dist[adjNode]=dis+edgeWeight
            heappush(pq,(dist[adjNode],adjNode))
            parent[adjNode]=node 

if dist[n]==float('inf'): #Means the target node which is n here is not reachable
    print(-1)
else:
    path = []
    node = n 
    while parent[node]!=node: # While we dont reach the src node, because parent of source == source node itself , it is backward traversal 
        path.append(node)
        node = parent[node]
    path.append(1) # Append the src node which is 1 here 
    path.reverse()
    print(*path)
