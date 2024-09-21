N = int(input())
v = int(input())
a = []

for i in range(0, N):
    a.append(int(input()))

# 線形探索
found_id = -1
for i in range(0, N):
    if (a[i] == v):
        found_id = i
        break

print(found_id)
