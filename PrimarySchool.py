from School import School


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickUpPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        schoolP =  super().__repr__()
        schoolP = schoolP + 'The pickup policy is {}'.format(self.pickupPolicy)
        

