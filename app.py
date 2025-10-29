import json
q = 0
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
for i in range(10000):
    print(data[q]['title'])
    q += 1
