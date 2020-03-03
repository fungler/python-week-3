class Course:

    def __init__(self, name, classroom, teacher, grade="none"):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.grade = grade

    def __repr__(self): 
       return 'Course(%r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.grade)     
  
    def __str__(self):
        return '{name}, {classroom}, {teacher}, {grade}.'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, grade=self.grade)
    
