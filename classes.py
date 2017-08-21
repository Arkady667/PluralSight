students = []

################# Konstrunktor (__init__) i __str__ ###############################
""" 
class Student:
    def __init__(self ,name, id=332): # self jest argumentem metody w klasie. Sluzy do wywolywania metody
        student = {
        "name": name,
        "id": id
        }
        students.append(student)

    def __str__(self):
        return "Student"


# student = Student()  # przechowuje adres
# student.add_student("Mark")
"""
###################### Atrybuty ########################################

class Student:

    school_name = "WAT"  # atrybut klasy wspolny dla wszystkich instancji

    def __init__(self, name, id=322):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.mame.capitalize()

    def get_school_name(self):
        return self.school_name

# mark = Student("Mark") # mark jest bezposrednio powiazany z funkcja __init__
# print(mark)

print(Student.school_name) # wywolanie prosto z klasy. Nie ma nawiasow bo to nie jest instancja, nie obchodzi go instancja

############################# Dziedziczenie ###################################


class UniversityStudent(Student): # ta klasa dziedziczy po klasie Student (parent) - UniversityStudent (derived)
                                  # Ma dostep do wszystkich metody i atryutow parenta

    school_name = "MIT"

    def get_school_name(self):    # Ta metoda nadpisze metode z parenta!
        return self.school_name


james = UniversityStudent("james") # nowa instancja
print(UniversityStudent.school_name)


