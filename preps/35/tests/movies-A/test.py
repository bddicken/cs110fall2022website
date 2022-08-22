import prep35

movie_collections = [{'terminator', 'matrix', 'avengers'}, {'terminator', 'john wick'}, {'indiana jones', 'terminator'}]
result = prep35.get_common_movies(movie_collections)
for movie in sorted(result):
    print (movie)
