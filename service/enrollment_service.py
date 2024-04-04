from model.enrollment import Enrollment

class EnrollmentService:
  def __init__(self):
    self.enrollment = Enrollment()

  def get_all(self):
    return [{'id':s[0], 'student_number':s[1], 'student_name':s[2], 'course_name':s[3], 'professor':s[4], 'credit':s[5],} for s in self.enrollment.get_all()]

  def add(self,enrollment_dto):
    return self.enrollment.add(enrollment_dto)

  def cancel(self, id):
    return self.enrollment.cancel(id)