def func(i, w, a):
    if i == 0:
        if w == 0:
            return True
        else:
            return False

    if (func(i - 1, w, a)):
        return True
    if (func(i - 1, w - a[i - 1], a)):
        return True

    return False

# 与えられる整数の数
N = int(input())
# 求める総和
W = int(input())
# a(list)から何個かの整数を選んで総和をWにできるか
a = list(map(int, input().split()))

if func(N, W, a):
    print('Yes')
else:
    print('No')
