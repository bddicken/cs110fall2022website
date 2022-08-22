import prep36

restricted = {'knife', 'razor', 'gun', 'TNT'}
carryon = {'clothes', 'gun', 'TNT'}
personal = {'knife', 'razor', 'gun', 'TNT'}
result = prep36.get_ok_items(carryon, personal, restricted)

for movie in sorted(result):
    print (movie)

