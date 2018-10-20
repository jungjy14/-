shape = { 1: {0: 1, 1: 3, 2: 0, 3: 2}, 2: {0: 2, 1: 3, 2: 1, 3: 0}, 3: {0: 2, 1: 0, 2: 3, 3: 1}, 4: {0: 3, 1: 2, 2: 0, 3: 1}, 5: {0: 2, 1: 3, 2: 0, 3: 1} }
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def goNext(arr, N, i, j, d, start):
    loop = 1
    _next = []
    while True:
        x = i + (dx[d] * loop)
        y = j + (dy[d] * loop)

        # 벽
        if x < 0 or x >= N or y < 0 or y >= N :
            _next = [x, y, shape[5][d]]
            # print('벽')
            break

        # 웜홀
        if arr[x][y] >= 6:
            # print('웜홀')
            if wormhole[arr[x][y]][0][0] == x and wormhole[arr[x][y]][0][1] == y :
                _next = [wormhole[arr[x][y]][1][0], wormhole[arr[x][y]][1][1], d]
            else :
                _next = [wormhole[arr[x][y]][0][0], wormhole[arr[x][y]][0][1], d]
            break
        # 네모
        if arr[x][y] == 5 :
            # print('네모')
            _next = [x, y, shape[5][d]]
            break

        # 세모 벽돌
        if arr[x][y] in [1, 2, 3, 4]:
            # print('세모')
            _next = [x, y, shape[arr[x][y]][d]]
            break

        # 시작점 또는 블랙홀
        if start[0] == x and start[1] == y:
            # print('시작점')
            _next = [-1, -1, -1]
            break
        if arr[x][y] == -1:
            # print('블랙홀')
            _next = [-1, -1, -1]
            break

        loop = loop + 1

    return _next

T = int(input())
for t in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]

    # 초기화
    wormhole = { 6: [], 7: [], 8: [], 9: [], 10: [] }
    blackhole = list()
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 6 :
                wormhole[arr[i][j]].append([i, j])
            elif arr[i][j] == -1 :
                blackhole.append([i, j])

    Max = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if arr[i][j] == 0:
                    x = i
                    y = j
                    d = k

                    count = 0
                    index = 0
                    while True:
                        _next = goNext(arr, N, x, y, d, [i,j])

                        if _next[2] == -1:
                            break
                        if _next[2] != d:
                            count = count + 1
                        x, y, d = _next

                    if count > Max :
                        Max = count

    print("#{} {}".format(t, Max))
