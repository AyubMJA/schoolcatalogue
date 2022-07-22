#from School import School
from HighSchool import HighSchool
from PrimarySchool import PrimarySchool
#ßfrom MiddleSchool import MiddleSchool

#Test for school.py
'''
mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.get_name())
print(mySchool.get_level())
mySchool.set_numberOfStudent(200)
print(mySchool.get_numberOfStudent())   
'''

#Test for Primary School

'''
testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.get_pickUpPolicy())
'''

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sportsTeam())
print(c)