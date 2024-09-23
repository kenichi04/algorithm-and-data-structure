memo = [-1] * 50

# 計算済の場合はメモ化（キャッシュ）
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if (memo[n] != -1):
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

fibo(49)
for i in range(50):
    print('{} 項目: {}'.format(i, memo[i]))
