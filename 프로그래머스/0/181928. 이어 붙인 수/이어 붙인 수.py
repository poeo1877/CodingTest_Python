def solution(num_list):
    odd = []
    even = []
    for num in num_list:
        if num%2:
            odd.append(f'{num}')
        else:
            even.append(f'{num}')
    
    odd = int(''.join(odd))
    even = int(''.join(even))
    return odd + even