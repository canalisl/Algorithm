import sys
sys.stdin = open('18258.txt')
input = sys.stdin.readline


def queueCommand(command):
    global head
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])
            # 실제로 값을 제거하지 않고, head만 우측으로 +1만큼 이동
            head += 1
    elif command[0] == 'size':
        print(len(queue) - head)
    elif command[0] == 'empty':
        if head == len(queue):
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])
    elif command[0] == 'back':
        # 큐가 빈 경우 = head(큐의 인덱스)가 큐의 끝(큐의 길이 - 1)을 초과한 경우 
        if head == len(queue):
            print(-1)
        else:
            print(queue[len(queue) - 1])


N = int(input())
queue = []
# 큐의 가장 앞 인덱스를 가리키는 변수
head = 0
for _ in range(N):
    command = input().rstrip().split()
    queueCommand(command)

