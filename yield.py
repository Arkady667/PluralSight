students = []

def read_file():
    try:
        f = open("students.txt", "r") # "r" wymaga aby plik istnial
        for student in read_students(f): #czyta kazda linie i dodaje do listy
            student.append(student)
        f.close()
    except Exception:
        print("Could not read file")

#generator

def read_students(f):
    for line in f:
        yield line


read_file()
print(students)