class Student:

    def __init__(self, name, gender, datasheet):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
    
    def __repr__(self): 
       return 'Student(%r, %r, %r)' % (self.name, self.gender, self.datasheet)     
  
    def __str__(self):
        return '{name}, {gender}, {datasheet}'.format(name=self.name, gender=self.gender, datasheet=self.datasheet)

    def get_avg_grade(self):
        pass

