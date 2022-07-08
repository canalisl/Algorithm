import sys
sys.stdin = open('18258.txt')
input = sys.stdin.readline


def queueCommand(command):
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[len(queue) - 1])


N = int(input())
queue = []
for _ in range(N):
    command = input().rstrip().split()
    queueCommand(command)

