'''
1. 한 번호가 다른 번호의 접두어인지 확인하기.
2. 접두어?
    구조대 119
    박준영 97 674 223
    지영석 11 9552 4421
   구조대 번호는 지영석 번호의 접두어다 : False 출력
   접두어가 아니면 True
3. 전화번호 길이 1 - 20
4. 중복 전화번호 없고 전화번호 길이는 최대 20이고, 문자열로 주어진다.
'''

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        length = len(phone_book[i-1])
        if phone_book[i-1] == phone_book[i][:length]:
            return False
    return True