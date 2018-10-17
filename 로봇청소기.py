def turn_robot(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2


def back_robot(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
arr = []
answer = 2

for i in range(0, N):
    temp = list(map(int, input().split()))
    arr.append(temp)

arr[r][c] = answer

while True:
    notClean = True
    for loop in range(0, 4):
        d = turn_robot(d)

        i = r + dx[d]
        j = c + dy[d]

        if i >= 0 and i < N and j >= 0 and j < M and arr[i][j] == 0:
            r = i
            c = j
            notClean = False
            answer = answer + 1
            arr[r][c] = answer
            break

    if notClean:
        r = r + dx[back_robot(d)]
        c = c + dy[back_robot(d)]

        if arr[r][c] == 1:
            break

# for k in arr:
#     for kk in k:
#         print("%02d" % kk, end=' ')
#     print()

print(answer-1)
