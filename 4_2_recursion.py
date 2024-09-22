def func(n):
    # 再帰呼び出しの確認
    # print('func {} の呼び出し'.format(n))

    if n == 0:
        return 0
    result = n + func(n - 1)

    print('{} までの和 = {}'.format(n, result))

    return result

func(5)
