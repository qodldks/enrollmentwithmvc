from model.lecture import Lecture

class LectureService:
  def __init__(self):
    self.lecture = Lecture()

  def get_all(self):
    return [{'id':s[0], 'professor_name':s[1], 'course_name':s[2], 'credit':s[3], 'major':s[4], 'day':s[5], 'start_time':s[6], 'end_time':s[7]} for s in self.lecture.get_all()]

  def add(self,dto):
    return self.lecture.add(dto)

  def delete(self,id):
    return self.lecture.delete(id)