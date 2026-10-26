registrations = [(101, "Python"),(101, "Maths"),(102, "Python"),(102, "Python"), (103, "Python"),(103, "Java")]
valid_courses = ("Python", "Maths", "Java")
invalid_pairs = (("Python", "Java"),)
students = [101, 102, 103]
for student in students:
    courses = []
    for reg in registrations:
        if reg[0] == student:
            courses.append(reg[1])
    print("\nStudent:", student)
    print("Courses:", courses)
    duplicate = False
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if courses[i] == courses[j]:
                duplicate = True
    if duplicate:
        print("Duplicate Registration Found")
    invalid = False
    for course in courses:
        if course not in valid_courses:
            invalid = True
    if invalid:
        print("Invalid Course Selected")
    combination = False
    for pair in invalid_pairs:
        if pair[0] in courses and pair[1] in courses:
            combination = True
    if combination:
        print("Invalid Course Combination")
    if not duplicate and not invalid and not combination:
        print("Registration Valid")