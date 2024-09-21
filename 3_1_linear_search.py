N = int(input())
v = int(input())
a = []

for i in range(0, N):
    a.append(int(input()))

# 線形探索
exist = False
for i in range(0, N):
    if (a[i] == v):
        exist = True

print('Yes' if exist else 'No')
