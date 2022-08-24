# 효율성테스트 3,4 시간초과
def solution(phone_book):
    answer = True
    for word in phone_book:
        for i in range(len(phone_book)):
            if word != phone_book[i] and word in phone_book[i][:len(word)]:
                answer = False
                return answer
    return answer

# 효율성테스트 3,4 시간초과
# 테스트케이스 실행시간 단축
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                return answer
    return answer