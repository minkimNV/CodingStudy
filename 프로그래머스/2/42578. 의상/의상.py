def solution(clothes):
    closet = {}
    for c in clothes:
        category = c[1]
        if category not in closet.keys():
            closet[category] = 1
        else:
            closet[category] += 1

    answer = 1
    for key in closet:
        answer *= (closet[key] + 1)


    return answer-1