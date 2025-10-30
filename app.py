# import json
# q = 0
# ## Open the JSON file of movie data
# movies = open("./movies.json", encoding="utf8")
# ## create variable "data" that represents the enitre movie list
# data = json.load(movies)
# for i in range(14117):
#     print(data[q]['title'])
#     q += 1

import json
q = 0
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for i in range(14117):
    print(data[q]['title'])
    q += 1