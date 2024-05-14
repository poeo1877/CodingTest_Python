def solution(phone_book):
##### 효율성 3, 4번 실패######
#     for phone_number in phone_book:
#         for item in phone_book:
#             # 접두어가 되려면 item의 길이가 더 길어야 한다.
#             if len(phone_number) >= len(item):
#                 continue
            
#             if phone_number == item[0: len(phone_number)]:
#                 return False

    # char 단위로 아스키 번호 순 정렬
    phone_book.sort()
    
    for index in range(len(phone_book) - 1):
        current_item = phone_book[index]
        next_item = phone_book[index + 1]
        
        if len(current_item) < len(next_item) and current_item == next_item[:len(current_item)]:
            return False
    
    
    return True