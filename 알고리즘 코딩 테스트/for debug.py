import sys
input = sys.stdin.readline

n = int(input())
seq_li = [0] * n

for i in range(n):
    seq_li[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    seq = seq_li[i]
    if seq >= num:
        while seq >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        if stack.pop() > seq:
            print("NO")
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)