import prep34

dict_data = {'a':'b', 'c':'d', 'e':'f'}
set_data = {'c', 'e'}
prep34.swap(dict_data, set_data)
for key in sorted(dict_data):
    print (key, '->', dict_data[key])

