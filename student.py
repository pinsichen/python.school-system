class Student:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.score = []

    def print(self):
        print(self.name)
        print(self.sex)
        print(self.score)

    def add_score(self, s):
        self.score.append(s)

    def average(self):
        total = 0.0
        for s in self.score:
            total = total + s
        return total/len(self.score)

