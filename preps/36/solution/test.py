import prep33

restricted = {'knife', 'water', 'razor'}
carryon = {'laptop', 'water', 'clothes'}
personal = {'mints', 'knife', 'keys'}
result = prep33.get_ok_items(carryon, personal, restricted)

for movie in sorted(result):
    print (movie)

