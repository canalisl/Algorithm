from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    terms_dict = defaultdict(int)
    for term in terms:
        terms_dict[term.split()[0]] = int(term.split()[1])
    
    for n in range(len(privacies)):
        date = (privacies[n].split()[0]).split(".")  # ["2019","01","01"]
        term_type = privacies[n].split()[1] # "A" 
        
        # 마지노선 날짜 변경
        # 년, 월 처리
        if int(date[1]) + terms_dict[term_type] > 12:
            date[0] = str(int(date[0]) + (int(date[1]) + terms_dict[term_type]) // 12)
            if (int(date[1]) + terms_dict[term_type]) % 12 < 10:
                date[1] = '0' + str((int(date[1]) + terms_dict[term_type]) % 12)
            else:
                date[1] = str((int(date[1]) + terms_dict[term_type]) % 12)
        else:
            if int(date[1]) + terms_dict[term_type] < 10:
                date[1] = '0' + str(int(date[1]) + terms_dict[term_type])
            else:
                date[1] = str(int(date[1]) + terms_dict[term_type])
        
        # 일 처리
        if int(date[2]) - 1 == 0:
            date[2] = '28'
            if int(date[1]) - 1 == 0:
                date[0] = str(int(date[0]) - 1)
                date[1] = '12'
            else:
                if int(date[1]) - 1 < 10:
                    date[1] = '0' + str(int(date[1]) - 1)
                else:
                    date[1] = str(int(date[1]) - 1)
        else:
            if int(date[2]) - 1 < 10:
                date[2] = '0' + str(int(date[2]) - 1)
            else:
                date[2] = str(int(date[2]) - 1)
        date = ".".join(date)


        # 연도 비교
        if int(date[:4]) < int(today[:4]):
            answer.append(n + 1)
            continue
        elif int(date[:4]) > int(today[:4]):
            continue
        else:   # 년도 같을때만
            # 월 비교
            if int(date[5:7]) < int(today[5:7]):
                answer.append(n + 1)
                continue
            elif int(date[5:7]) > int(today[5:7]):
                continue
            else:   # 월 같을때만
                # 일 비교
                if int(date[8:]) < int(today[8:]):
                    answer.append(n + 1)
                    continue
                else:
                    pass
    answer.sort()
    return answer