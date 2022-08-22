import prep35

collections = [{'Sherlock', 'Mighty Ducks', 'T2', 'John Wick'}, 
               {'John Wick', 'Mighty Ducks', 'T3'}, 
               {'John Wick', 'Mighty Ducks'}, 
               {'Alita', 'John Wick', 'T2', 'Mighty Ducks'}]
result = prep35.get_common_movies(collections)
for movie in sorted(result):
    print (movie)
