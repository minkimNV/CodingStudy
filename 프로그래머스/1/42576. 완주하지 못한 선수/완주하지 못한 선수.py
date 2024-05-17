'''
1. 참가 선수, 완주 선수: 무조건 한 명이 완주 못함.
-> len(completion) = len(participant) - 1
2. 완주 못한 선수 이름 return
3. 동명이인 쌉가능
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
