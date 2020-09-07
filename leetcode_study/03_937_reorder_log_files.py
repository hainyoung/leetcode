from typing import List

def log_1(logs: List[str]):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)

        else :
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters+digits

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

# let1 art can
# x.split()[1:] : art can(식별자 뒷부분)
# x.split()[0] : let1(식별자)
# 식별자 뒤의 문자순서대로 나열하는데 문자가 동일하면 식별자 순서대로
# 숫자 로그는 입력 순서대로이기 때문에 따로 정렬할 필요가 없다



print(log_1(logs))