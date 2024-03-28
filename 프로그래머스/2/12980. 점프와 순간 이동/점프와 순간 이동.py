# 2로 나눠 떨어지면 순간이동 가능. 아니면 1칸 점프
def solution(n):
    ans = 1
    while n > 1:
        if n/2 > int(n/2):
            n -= 1
            ans += 1
        else:
            n = n // 2

    return ans