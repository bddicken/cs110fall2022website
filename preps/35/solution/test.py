import prep32

movie_collections = [{'terminator', 'matrix', 'avengers'}, {'terminator', 'john wick'}, {'indiana jones', 'terminator'}]
result = prep32.get_common_movies(movie_collections)
for movie in sorted(result):
    print (movie)
