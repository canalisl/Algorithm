import sys
sys.stdin = open('2941.txt')
input = sys.stdin.readline


def croatian_count(word):
    # 여기서는 global로 전역변수 참조 안해도 되는 이유?
    for croatian in croatian_alphabet:
    # if문으로 체크 안해도 됨
        word = word.replace(croatian, '*')
    return len(word)


word = input().rstrip()
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
print(croatian_count(word))
