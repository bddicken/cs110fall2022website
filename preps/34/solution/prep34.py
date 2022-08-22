
def swap(dict_data, keys):
    dict_keys = list(dict_data.keys())
    for key in dict_keys:
        if key in keys:
            val = dict_data[key]
            dict_data[val] = key
            del dict_data[key]

'''
def main():
    dict_data = {'a':'b', 'c':'d', 'e':'f'}
    set_data = {'c', 'e'}
    swap(dict_data, set_data)
    print(dict_data)
    
    dict_data = {23:24, 110:120, 50:45, 70:50, 57:1}
    set_data = {23, 110, 57}
    swap(dict_data, set_data)
    print(dict_data)
    
main()
'''

