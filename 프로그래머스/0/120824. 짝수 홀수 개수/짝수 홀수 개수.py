def solution(num_list):
    answer = [num%2==0 for num in num_list]
    return [answer.count(True), answer.count(False)]