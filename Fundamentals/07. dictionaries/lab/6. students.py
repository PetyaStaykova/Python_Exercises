data = input()
courses = {}

while ':' in data:
    name, i_d, course = data.split(':')
    if course not in courses:
        courses[course] = {}
    courses[course][i_d] = name
    data = input()

searched_course = data
searched_course_as_list = searched_course.split('_')
searched_course = ' '.join(searched_course_as_list)

for course in courses:
    if course == searched_course:
        for i_d, name in courses[course].items():
            print(f'{name} - {i_d}')