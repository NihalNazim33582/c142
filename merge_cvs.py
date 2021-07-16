import csv

with open('Movies - Movies.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    print(len(all_movies))
    headers=data[0]
    headers.append('picture_links')
    print(headers)

with open('final.csv','a+',encoding='utf8') as f:
    csvWriter=csv.writer((f))
    csvWriter.writerow(headers)

with open('movie_links.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies_links=data[1:]
    print(len(all_movies_links))


for movie_item in all_movies:
    findpicture=any(movie_item[8] in movies_links_item for movies_links_item in all_movies_links)
    if findpicture:
        for item in all_movies_links:
            if movie_item[8] == item[0]:
                movie_item.append(item[1])
                if len(movie_item) == 28:
                    with open('final.csv','a+',encoding='utf8') as f:
                        csvWriter=csv.writer(f)
                        csvWriter.writerow(movie_item)