students = int(input('Students:\n'))
c_cap = int(input('Classroom capacity:\n'))
t_cap = int(input('Table Capacity:\n'))

classrooms = students / c_cap
groups = students / t_cap
size = students % t_cap

print('Classrooms needed:', classrooms) 
print('Groups needed:', groups) 
print('Size of extra group:', size) 

