'''
1. 총 N 마리 중 N / 2 마리 소유 가능
2. nums = [3, 1, 2, 3] : 4마리의 폰켓몬, 2마리의 3번, 각각 1마리의 1번과 2번 폰켓몬이 있다는 의미
3. 최대한 많은 종류 가지기
4. 4마리일 경우 2마리 가질 수 있고, 최대한 많은 종류라면 2마리 모두 각각 다른 종류여야 함; 출력값 2
'''

def solution(nums):
    types = set(nums)               # 폰켓몬 몇 종류 있죠
    if len(nums)/2 < len(types):    # 종류 수 보다 가질 수 있는 수가 더 적으면
        return len(nums)/2          # 가질 수 있는 수 출력
    return len(types)               # 그렇지 않으면 종류 수 만큼 출력



# nums = [3, 1, 2, 3]
# nums = [3, 3, 3, 2, 2, 4]
# nums = [3, 3, 3, 2, 2, 2]

# print(solution(nums))