# #########################################################
# #funkcja z nieograniczona liczba argumentow
#
# def var_args( name, *args): #variable arguments - *args
#     print(name)
#     print(args)
#
# var_args("Mark", "Python", True, False, None, 123)
#
# #funkcja z neograniczona liczba argumentow + keywords
#
# def var_kwargs( name, **kwargs): #variable arguments - *args
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])
#
# var_kwargs("Mark", description="Python", feedback=None)
# ############################################################
# add_student(name="Mark", id=144) #144 nadpisuje 332
# #############################################################


students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


#druga funkcja i pierwsza maja powtorzenia, ktore usuwam my zoptymalizowac kod

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, id=332): #student id jest zainicjalizowana jako 332 ale moze zostac
    student = {                #nadpisana przez wywolanie funkcji i dodanie innej wartosc
        "name": name,
        "id": id
    }
    students.append(student)

##### Pliki ##############3

# Zapis

def save_file(student):
    try:
        f =open("students.txt", "a")   #student.txt nie musi istniec, "a" oznacza ze bedzie w pliku tekst
        f.write(student+"\n")          # "w" - writing (nadpisuje caly plik
        f.close()                      # "r" - reading a text file
    except Exception:                  # "a" - appending (do nowego pliku - dodawanie danych
        print("Coud not save file")    # "rb", "rw" - reading or writing to binary file

# Odczyt

def read_file():
    try:
        f = open("students.txt", "r") # "r" wymaga aby plik istnial
        for student in f.readlines(): #czyta kazda linie i dodaje do listy
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


#student_list = get_students_titlecase()

read_file()
print_students_titlecase()

student_name = raw_input("Enter student name: ")
student_id = input("Enter student ID: ")
add_student(student_name, student_id)

save_file(get_students_titlecase())

#print_students_titlecase()

