T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    num = input().strip()

    line = int(N / 4)

    sum = set()
    for j in range(line):
        for k in range(4):
            sum.add(int(num[k * line:(k + 1) * line], 16))
        num = num[-1] + num[:-1]

    answer = list(sum)
    answer.sort(reverse=True)
    print('#{} {}'.format(i + 1, answer[K-1]))
