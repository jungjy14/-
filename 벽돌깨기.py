import copy

answer = list()

def dfs(arr, depth, N, W, H):
    if depth == N:
        answer.append(getRemain(arr))
    else:
        for j in range(W):
            visit = copy.deepcopy(arr)
            i = getTop(arr, H, j)

            if i >= 0 and arr[i][j] > 0:
                q = [[i, j]]

                while len(q) > 0:
                    x, y = q.pop(0)
                    visit[x][y] = 0
                    for dx in range(1, arr[x][y]):
                        if x+dx < 0 or x+dx >= H:
                            break

                        if arr[x+dx][y] > 0 and visit[x+dx][y] > 0:
                            q.append([x+dx, y])
                            visit[x+dx][y] = 0

                    for dx in range(1, arr[x][y]):
                        if x-dx < 0 or x-dx >= H:
                            break

                        if arr[x-dx][y] > 0 and visit[x-dx][y] > 0:
                            q.append([x-dx, y])
                            visit[x-dx][y] = 0

                    for dy in range(1, arr[x][y]):
                        if y+dy < 0 or y+dy >= W:
                            break

                        if arr[x][y+dy] > 0 and visit[x][y+dy] > 0:
                            q.append([x, y+dy])
                            visit[x][y+dy] = 0

                    for dy in range(1, arr[x][y]):
                        if y-dy < 0 or y-dy >= W:
                            break

                        if arr[x][y-dy] > 0 and visit[x][y-dy] > 0:
                            q.append([x, y-dy])
                            visit[x][y-dy] = 0

                visit = removeEmpty(visit, W, H)
                dfs(visit, depth+1, N, W, H)

            else:
                dfs(visit, depth+1, N, W, H)


def getRemain(arr):
    count = 0
    for row in arr:
        for col in row:
            if col > 0:
                count = count + 1
    return count


def getTop(arr, H, j):
    top = -1
    for i in range(H):
        if arr[i][j] > 0:
            top = i
            break
    return top

def removeEmpty(arr, W, H):
    temp = [[0] * W for _ in range(H)]
    for j in range(W):
        q = list()
        for i in range(H):
            if arr[i][j] > 0:
                q.append(arr[i][j])
        q.reverse()
        for index, value in enumerate(q):
            temp[-(index+1)][j] = value

    return temp

T = int(input())

for test_case in range(1, T + 1):
    answer = list()
    N, W, H = list(map(int, input().split()))

    arr = list()
    for i in range(H):
        arr.append(list(map(int, input().split())))

    dfs(arr, 0, N, W, H)

    print('#{} {}'.format(test_case, min(answer)))

