class School:
    def __init__(self):
        print("Welcome to school")
        self.students = []

    def add_student(self, s):
        self.students.append(s)

    def print(self):
        print("Total List of Students")
        for s in self.students:
            print("{} {} {}".format(s.name, s.sex, s.score))

    def get_student(self, name):
        for s in self.students:
            print(s.name)
            if s.name == name:
                return s

