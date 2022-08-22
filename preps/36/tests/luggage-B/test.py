import prep36

restricted = {'knife', 'big shampoo'}
carryon = {'knife', 'camera', 'headphones', 'clothes'}
personal = {'gum', 'knife'}
result = prep36.get_ok_items(carryon, personal, restricted)

for movie in sorted(result):
    print (movie)

