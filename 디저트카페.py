dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

answer = list()

def dfs(arr, N, depth, path):
    if(depth > 1 and path['start'][0] == path['trace'][-1][0] and path['start'][1] == path['trace'][-1][1]):
        answer.append(depth)
    else:
        d = path['trace'][-1][2]

        for i in range(4):
            x = path['trace'][-1][0] + dx[i]
            y = path['trace'][-1][1] + dy[i]
            
            # 범위 벗어남
            if x < 0 or x >= N or y < 0 or y >= N:
                continue

            # 현재 방향의 반대 방향
            if i == (d + 2) % 4:
                continue

            isVisit = False
            for p in path['trace']:
                # 이전에 진행했던 방향
                if i == p[2] and i != d:
                    isVisit = True
                    break
                # 이미 방문한 좌표
                if x == p[0] and y == p[1]:
                    isVisit = True
                    break
                # 이미 방문한 동일한 가게
                if arr[x][y] == arr[p[0]][p[1]]:
                    isVisit = True
                    break
            
            if isVisit == False:
                path['trace'].append([x, y, i])
                dfs(arr, N, depth+1, path)            
                path['trace'].pop(-1)


T = int(input())

for t in range(1, T+1):
    N = int(input())

    answer.clear()

    arr = list()
    for i in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            x = i + dx[0]
            y = j + dy[0]
            
            # 범위 벗어남
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            path = {
                'start': [i, j],
                'trace': [[x, y, 0]]
            }
            dfs(arr, N, 1, path)

    if len(answer) == 0:
        print('#{} -1'.format(t))
    else:
        answer.sort(reverse=True)
        print('#{} {}'.format(t, answer[0]))