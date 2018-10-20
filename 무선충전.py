dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

N = 10
def isCharge(ap, man):
    D = abs(man['x']-ap[0]) + abs(man['y']-ap[1])
    if D <= ap[2]:
        return True
    else:
        return False


T = int(input())
for t in range(1, T+1):
    people = [{'x': 1, 'y': 1, 'charge': []}, {'x': 10, 'y': 10, 'charge': []}]

    M, A = list(map(int, input().split()))
    path = [list(map(int, input().split())) for _ in range(2)]
    AP = [list(map(int, input().split())) for ap in range(A)]

    for man in people:
        temp = []
        for index, ap in enumerate(AP):
            if isCharge(ap, man):
                temp.append(index+1)
        temp.sort(key=lambda x: AP[x-1][3], reverse=True)
        man['charge'].append(temp)

    for i in range(M):
        for j in range(2):
            people[j]['x'] = people[j]['x'] + dx[path[j][i]]
            people[j]['y'] = people[j]['y'] + dy[path[j][i]]

            temp = []
            for index, ap in enumerate(AP):
                if isCharge(ap, people[j]):
                    temp.append(index + 1)
            temp.sort(key=lambda x: AP[x-1][3], reverse=True)
            people[j]['charge'].append(temp)

    # print(people[0])
    # print(people[1])

    answer = []
    tempList = []
    for i in range(M+1):
        temp = [0, 0]
        if len(people[0]['charge'][i]) > 0:
            temp[0] = people[0]['charge'][i][0]
        if len(people[1]['charge'][i]) > 0:
            temp[1] = people[1]['charge'][i][0]

        if (temp[0] != 0 and temp[1] != 0) and temp[0] == temp[1]:
            a = 0
            b = 0

            if len(people[0]['charge'][i]) > 1:
                a = AP[people[0]['charge'][i][1]-1][3]
            if len(people[1]['charge'][i]) > 1:
                b = AP[people[1]['charge'][i][1]-1][3]

            j = -1
            if a < b:
                j = 1
            elif a > b:
                j = 0
            elif a == b and a != 0 and b != 0:
                j = 0

            if j != -1:
                temp[j] = people[j]['charge'][i][1]

        _sum = 0
        if temp[0] != 0:
            _sum = _sum + AP[temp[0]-1][3]
        if temp[1] != 0:
            _sum = _sum + AP[temp[1]-1][3]
        if temp[0] == temp[1] and (temp[0] != 0 and temp[1] != 0):
            _sum = int(_sum / 2)
        answer.append(_sum)
        tempList.append(temp)

    # for k in range(M):
    #     print(people[0]['charge'][k])
    #     print(people[1]['charge'][k])
    #     print(tempList[k])
    #     print(answer[k])
    #     print('')

    print("#{} {}".format(t, sum(answer)))
    people.clear()






