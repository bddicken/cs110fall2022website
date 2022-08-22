import prep35

collections = [{'Sherlock', 'Mighty Ducks', 'T2', 'John Wick', 'T3'}, 
               {'John Wick', 'Sherlock', 'Mighty Ducks', 'T3'}, 
               {'John Wick', 'Sherlock', 'T3'}, 
               {'Alita', 'John Wick', 'T2', 'T3', 'Sherlock', 'Mighty Ducks'}]
result = prep35.get_common_movies(collections)
for movie in sorted(result):
    print (movie)
