N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
opList = []
res = []


def cal():
    i = 0
    answer = num[i]
    for op in opList:
        if op == 0:
            answer = answer + num[i+1]
        elif op == 1:
            answer = answer - num[i+1]
        elif op == 2:
            answer = answer * num[i+1]
        elif op == 3:
            answer = int(answer / num[i+1])

        i = i + 1
    return answer


def dfs(depth):
    if depth == N-1:
        res.append(cal())
    else:
        for i in range(len(operator)):
            if operator[i] > 0:
                operator[i] = operator[i] - 1
                opList.append(i)

                dfs(depth + 1)

                operator[i] = operator[i] + 1
                opList.pop()


dfs(0)

print(max(res))
print(min(res))
