class Datasheet:

    def __init__(self, lstCourses):
        self.lstCourses = lstCourses
    
    def __repr__(self): 
       return 'Datasheet(%r)' % (self.lstCourses)     
  
    def __str__(self):
        return '{lst}'.format(lst=self.lstCourses)

    def get_grades_as_list(self):
        pass
