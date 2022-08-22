import prep34

dict_data = {23:24, 110:120, 50:45, 70:50, 57:1}
set_data = {23, 110, 57}
prep34.swap(dict_data, set_data)
for key in sorted(dict_data):
    print (key, '->', dict_data[key])

