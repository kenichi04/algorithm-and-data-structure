f = []
f.append(0)
f.append(1)

for i in range(2, 50):
    f.append(f[i - 1] + f[i - 2])
    print('{} 項目: {}'.format(i, f[i]))
