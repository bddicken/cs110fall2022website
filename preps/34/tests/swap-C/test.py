import prep34

dict_data = {20:25, 30:31}
set_data = {20}
prep34.swap(dict_data, set_data)
for key in sorted(dict_data):
    print (key, '->', dict_data[key])
