from model.course import Course

class CourseService:
  def __init__(self):
    self.course = Course()

  def get_all(self):
    return [{'id':s[0],'name':s[1], 'professor':s[2], 'credit':s[3]} for s in self.course.get_all()]

  def add(self, course_dto):
    self.check_duplication(course_dto)
    return self.course.add(course_dto)

  def check_duplication(self, course_dto):
    results = self.course.select_by_name(course_dto)
    if results is not None:
      for c in results:
        if c[1] == course_dto.name and c[2] == course_dto.professor:
          raise Exception("이미 등록된 과목입니다.")