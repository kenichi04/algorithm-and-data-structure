
N = int(input())
costs = list(map(int, input().split()))
# 十分大きい値とする
dp = [1000000] * N
# 初期条件
dp[0] = 0

for i in range(N):
    if i + 1 < N:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(costs[i] - costs[i + 1]))
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(costs[i] - costs[i + 2]))

print(dp[N - 1])
