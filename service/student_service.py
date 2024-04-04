from model.student import Student

class StudentService:
  def __init__(self):
    self.student = Student()

  def get_all(self):
    return [{'id':s[0],'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.student.get_all()]

  def get(self, student_number):
    return self.student.get(student_number)
  
  def add(self, student_dto):
    if self.get(student_dto.number) is not None:
      raise Exception("중복된 번호입니다.")
    return self.student.add(student_dto)