# def solution(genres, plays):

#     songs = [[genre, (play, i)] for genre, (play, i) in zip(genres, enumerate(plays))]
#     songs = sorted(songs, key = lambda x: (x[0], -x[1][1], x[1][0]))


#     # 재생횟수 많은 장르 찾기
#     gorder = {}
#     for i in range(len(songs)):
#         if songs[i][0] not in gorder:
#             gorder[songs[i][0]] = songs[i][1][1]
#         else:
#             gorder[songs[i][0]] += songs[i][1][1]

#     sortedgorder = sorted(gorder.items(), key=lambda x: -x[1])

#     # 상위 2 곡 인덱스
#     answer = []
#     cnt = 0
#     for genre in sortedgorder:
#         cnt = 0
#         for song in songs:
#             if genre[0] == song[0]:
#                 cnt += 1
#                 if cnt > 2 :
#                     break
#                 else:
#                     answer.append(song[1][0])

#     return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

def solution(genres, plays):
    answer = []

    songs = []
    for genre, (play, i) in zip(genres, enumerate(plays)):
        songs.append([genre, (play, i)])
    print(songs)

    genre_sort = sorted(songs, key = lambda x: (x[0], -x[1][1], x[1][0]))
    print(genre_sort)

    total_play = {}
    for song in genre_sort:
        if song[0] not in total_play:
            total_play[song[0]] = song[1][1]
        else:
            total_play[song[0]] += song[1][1]

    total_play = dict(sorted(total_play.items(), key = lambda x: -x[1]))
    print(total_play)

    for genre, _ in total_play.items():
        cnt = 0
        for g, (p, i) in genre_sort:
            if g == genre:
                cnt += 1
                answer.append(p)
                if cnt == 2:
                    break

    return answer
