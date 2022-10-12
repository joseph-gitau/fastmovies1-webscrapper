import re
import time

import requests
from bs4 import BeautifulSoup
import csv


def init_csv():
    movies = ['The Matrix', 'Shershaah', 'Once Upon a Time... In Hollywood', 'Wind River',
              "Harry Potter and the Sorcerer's Stone"
              ]
    years = ['1999', '2021', '2019', '2017', '2001']
    i = 0
    all_movies = []
    unavailable = []
    for movie in movies:
        temp = []
        lower_movie = movie.lower()
        clean = re.sub('[^A-Za-z0-9]+', '-', lower_movie)
        # join the movie name with the year
        movie_year = clean + '-' + years[i]
        print(i)
        i += 1
        page = requests.get('https://yts.mx/movies/' + movie_year)
        soup = BeautifulSoup(page.content, 'html.parser')
        # find the movie name
        movie_name = soup.find(id="vp_choose_quality")
        # check if movie_name is not None
        if movie_name is not None:
            option_list = movie_name.findAll('option')
            # loop through the option_list
            for option in option_list:
                temp.append({
                    'movie_name': movie,
                    'torrent_id': option['value'],
                    'quality': option.text
                })
            all_movies.append(temp)
        else:
            unavailable.append(movie)

    # write the data to a csv file
    with open('movies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['movie_name', 'torrent_id', 'quality'])
        for movie in all_movies:
            for torrent in movie:
                writer.writerow([torrent['movie_name'], torrent['torrent_id'], torrent['quality']])

    # write the unavailable movies to a csv file
    with open('unavailable.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['movie_name'])
        for movie in unavailable:
            writer.writerow([movie])

    print(f"Available movies: {all_movies}")
    print(f"Unavailable movies: {unavailable}")


def from_csv():
    start = time.time()
    i = 0
    all_movies = []
    unavailable = []
    counter = 0

    with open('Book1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # execute 10 times
            # if counter == 10:
            #     break
            counter += 1
            # print(row[1])
            temp = []
            lower_movie = row[1].lower()
            clean = re.sub('[^A-Za-z0-9]+', '-', lower_movie)
            # join the movie name with the year
            movie_year = clean + '-' + row[2]
            print(i)
            i += 1
            page = requests.get('https://yts.mx/movies/' + movie_year)
            soup = BeautifulSoup(page.content, 'html.parser')
            # find the movie name
            movie_name = soup.find(id="vp_choose_quality")
            # check if movie_name is not None
            if movie_name is not None:
                option_list = movie_name.findAll('option')
                # loop through the option_list
                for option in option_list:
                    temp.append({
                        'a_id': row[0],
                        'movie_name': row[1],
                        'year': row[2],
                        'torrent_id': option['value'],
                        'quality': option.text
                    })
                all_movies.append(temp)
            else:
                unavailable.append({
                    'a_id': row[0],
                    'movie_name': row[1],
                })

    # write the data to a csv file
    with open('movies_all.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['a_id', 'movie_name', 'year', 'torrent_id', 'quality'])
        for movie in all_movies:
            for torrent in movie:
                writer.writerow([torrent['a_id'], torrent['movie_name'], torrent['year'], torrent['torrent_id'], torrent['quality']])

    # write the unavailable movies to a csv file
    with open('unavailable_all.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['a_id', 'movie_name'])
        for movie in unavailable:
            writer.writerow([movie['a_id'], movie['movie_name']])

    end = time.time()
    print(f"Time of execution = {end - start}")


if __name__ == '__main__':
    # init_csv()
    from_csv()
