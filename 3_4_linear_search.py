INF = 20000000

N = int(input())
# K以上の最小値のペアを探す
K = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 線形探索
min_value = INF
for i in range(N):
    for j in range(N):
        current = a[i] + b[j]
        if (current < K):
            continue

        if (current < min_value):
            min_value = current

print(min_value)
