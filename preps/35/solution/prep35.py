
def get_common_movies(movies):
    common = movies[0]
    for movie in movies:
        common = common.intersection(movie)
    return common

'''
def main():
    collections = [{'terminator', 'matrix', 'avengers'}, {'terminator', 'john wick'}, {'indiana jones', 'terminator'}]
    result = get_common_movies(collections)
    print(result)
    
    collections = [{'Sherlock', 'Mighty Ducks', 'T2', 'John Wick'}, 
                   {'John Wick', 'Mighty Ducks', 'T3'}, 
                   {'John Wick', 'Mighty Ducks'}, 
                   {'Alita', 'John Wick', 'T2', 'Mighty Ducks'}]
    result = get_common_movies(collections)
    print(result)
    
main()
'''

