import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [[0, 0]] 
for _ in range(N):
    W, V = map(int, input().split())
    items.append([W, V])

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):   
    weight = items[i][0]        
    value = items[i][1]         
    
    for w in range(1, K + 1):   
        if w < weight:
            dp[i][w] = dp[i-1][w] 
             
        else:
            dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight]) 
            
            
print(dp[N][K])