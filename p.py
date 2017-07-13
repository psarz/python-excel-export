class cricketer(object):
    def __init__(self, ipl_team, skills_in_cricket, name):
        self.ipl_team = ipl_team
        self.skills_in_cricket = skills_in_cricket
        self.name = name

    def fullname(self):
        return '{}{}'.format(self.name)

class worldcup(cricketer):
    pass

cric_1 = cricketer('mumbai', 'batsman', 'Rohit')
cric_2 = cricketer('Rcb', 'batsman', 'abdeviliers')
    
print(cric_1.ipl_team)
print(cric_2.skills_in_cricket)
