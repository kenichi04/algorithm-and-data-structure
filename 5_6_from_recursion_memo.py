INF = 2 ** 6  # 十分大きい値とする
dp = []

def rec(i):
    # dpの値が更新済み（メモ化）
    if dp[i] < INF:
        return dp[i]
    # ベースケース
    if i == 0:
        return 0

    # 足場i - 1から来た場合
    result = min(INF, rec(i - 1) + abs(costs[i] - costs[i - 1]))
    # 足場i - 2から来た場合
    if i > 1:
        result = min(result, rec(i - 2) + abs(costs[i] - costs[i - 2]))

    # メモ
    dp[i] = result
    return result

N = int(input())
costs = list(map(int, input().split()))
dp = [INF] * N

print(rec(N - 1))
