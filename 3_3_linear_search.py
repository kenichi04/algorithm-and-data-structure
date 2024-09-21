INF = 20000000  # 最小値はこの値未満と仮定
N = int(input())
a = []

for i in range(0, N):
    a.append(int(input()))

# 線形探索
min_value = INF
for i in range(0, N):
    min_value = min(min_value, a[i])

print(min_value)
