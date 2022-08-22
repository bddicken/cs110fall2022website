
def get_ok_items(carryon_contents, personal_contents, restricted):
    result_a = carryon_contents.difference(restricted)
    result_b = personal_contents.difference(restricted)
    return result_a.union(result_b)

'''
def main():
    restricted = {'knife', 'water', 'razor'}
    carryon = {'laptop', 'water', 'clothes'}
    personal = {'mints', 'knife', 'keys'}
    result = get_ok_items(carryon, personal, restricted)
    print(result)
    
main()
'''

