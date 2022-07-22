from hashlib import new


class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
        
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_numberOfStudent(self):
        return self.numberOfStudents

    def set_numberOfStudent(self,newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents


    def __repr__(self):
        school = "A {} school name {} with {} numberOfStudents".format(self.level, self.name, self.numberOfStudents)
        return school




