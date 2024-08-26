n, m = map(int, input().split())

node_connections = dict()

for i in range(1, n+1):
    node_connections[i] = []

# vertex info update
for _ in range(m):
    node1, node2 = map(int, input().split())
    
    node_connections[node1].append(node2)
    node_connections[node2].append(node1)


visited_status = [False for _ in range(n+1)]

def dfs(node):
    global visited_status
    visited_status[node] = True
    for n in node_connections[node]:
        if visited_status[n] == False:
            dfs(n)

ans_cnt = 0

for curr_search_node in range(1, n+1):
    if visited_status[curr_search_node] == False:
        dfs(curr_search_node)
        ans_cnt += 1

print(ans_cnt)
