def next_direction(direction):
    return (direction + 1) % 4


answer = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visit = [[0] * 101 for _ in range(101)]

N = int(input())

dragonList = []

for i in range(N):
    _input = list(map(int, input().split()))
    dragonList.append(_input)

for i, dragon in enumerate(dragonList):
    x, y, d, g = map(int, dragon)

    trace = {
        'start': [x, y],
        'direction': [d]
    }

    for generation in range(g):
        reversed_trace = list(reversed(trace['direction']))
        for k in reversed_trace:
            d = next_direction(k)
            trace['direction'].append(d)

    # print(trace)

    visit[y][x] = i+1
    for flow in trace['direction']:
        x = x + dx[flow]
        y = y + dy[flow]
        visit[y][x] = i+1

    # print(str(i+1), '드래곤')
    # for v in visit[:15]:
    #     print(v[:15])
    # print('')


for i in range(100):
    for j in range(100):
        if i+1 <= 100 or j+1 <= 100:
            if visit[i][j] > 0 and visit[i+1][j] > 0 and visit[i][j+1] > 0 and visit[i+1][j+1] > 0:
                answer = answer + 1
print(answer)
