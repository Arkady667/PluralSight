import student

class UniversityStudent(student.Student):

school_name = "MIT"

def get_school_name(self):    # Ta metoda nadpisze metode z parenta!
    return self.school_name
