"""
N個先までの移動コストの最小値の総和を求める
移動は一つ先もしくは二つ先への移動のどちらか
"""
N = int(input())
# i番目への移動コスト
cost = list(map(int, input().split()))
# i番目への移動コストの最小値の総和のメモ
dp = [0]

for i in range(1, N):
    if (i == 1):
        dp.append(abs(cost[i] - cost[i - 1]))
    else:
        val = min(dp[i - 1] + abs(cost[i] - cost[i - 1]),
                  dp[i - 2] + abs(cost[i] - cost[i - 2]))
        dp.append(val)

print(dp[N - 1])
