# def solution(genres, plays):
#     answer = []

#     dic = {}

#     for i in range(len(genres)):
#         if genres[i] in dic:
#             dic[genres[i]].append([plays[i],i])
#         else:
#             dic[genres[i]] = [[plays[i],i]]
    
    
#     genre_rank = {}

#     for genre in dic:
#         songs = dic[genre]
#         play_sum = 0
#         for song in songs:
#             play_sum += song[0]
        
#         genre_rank[genre] = play_sum
    
#     genre_rank = sorted(genre_rank.items(), key = lambda x : -x[1])

#     for genre in genre_rank:
#         song_rank = sorted(dic[genre[0]],key=lambda x : (-x[0],x[1]))
#         best = 0
#         for song in song_rank:
#             if best == 2:
#                 break
#             else:
#                 answer.append(song[1])
#                 best += 1
            
#     return answer

# g = ["classic", "pop", "classic", "classic", "pop"]
# p = [500, 600, 150, 800, 2500]

# print(solution(g,p))

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]

song_list = {e : [] for e in g}
genre_cnt = {e : 0 for e in g}

answer = []

for i in range(len(g)):
    song_list[g[i]].append([p[i],i])

for i in song_list:
    song_list[i] = sorted(song_list[i], key=lambda x : (-x[0],x[1]))
    for song in song_list[i]:
        genre_cnt[i] += song[0]

genre_cnt = sorted(genre_cnt.items(),key=lambda x : -x[1])


for genre in genre_cnt:
    cnt = 0
    for songs in song_list[genre[0]]:
        if cnt == 2:
            break
        else:
            cnt += 1
            answer.append(songs[1])

print(answer)