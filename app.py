# import json
# q = 0
# ## Open the JSON file of movie data
# movies = open("./movies.json", encoding="utf8")
# ## create variable "data" that represents the enitre movie list
# data = json.load(movies)
# for i in data:
#     print(data[q]['title'])
#     q += 1

# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)
# x = int(input("Imput?:"))
# for i in data:
#     if int(i['year']) >= x:
#         print(i ['year'], i ['title'])

# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)
# x = int(input("Imput?:"))
# y = int(input("Imput 2?:"))
# for i in data:
#     if int(i['year']) >= x:
#         if int(i['year']) <= y:
#             print(i ['year'], i ['title'])

# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)
# x = int(input("Imput?:"))
# for i in data:
#     if int(i['year']) >= x:
#         if int(i['year']) <= x:
#             print(i ['year'], i ['title'])

# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)        
# Search = input("what movie title?")
# for i in data:
#     if (i['title']) == Search:
#         print (i['year'], i['title'], i['cast'], i['genres'])

import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)        
Search = input("what movie genres?")
for i in data:
    if Search in i['genres']:
        print (i['year'], i['title'], i['cast'], i['genres'])