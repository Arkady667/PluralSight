

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