from School import School
class HighSchool(School):
    def __init__(self, name, numberOfStudents, **sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeam = sportsTeams

    def get_sportsTeam(self):
        return self.sportsTeam
    
    def __repr__(self):
        schoolH =  super().__repr__()
        return schoolH  + ' The sports team are:' + ', '.join(self.sportsTeam) + '.'