def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False

    return answer

    # startswith ==> 신기하네...