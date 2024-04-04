class CourseFormDTO:
  def __init__(self, name, professor, credit):
    self._name = name
    self._professor = professor
    self._credit = credit

  @property
  def name(self):
    return self._name

  @property
  def professor(self):
    return self._professor

  @property
  def	credit(self):
    return self._credit


class StudentFormDTO:
  def __init__(self, number, name, gender):
    self._number = number
    self._name = name
    self._gender = gender

  @property
  def number(self):
    return self._number

  @property
  def name(self):
    return self._name

  @property
  def gender(self):
    return self._gender
  

class EnrollmentFormDTO:
  def __init__(self, student_id, course_id):
    self._student_id = student_id
    self._course_id = course_id

  @property
  def student_id(self):
    return self._student_id

  @property
  def course_id(self):
    return self._course_id

class ProfessorFormDTO:
  def __init__(self, name, major, email):
    self._name = name
    self._major = major
    self._email = email

  @property
  def name(self):
    return self._name

  @property
  def major(self):
    return self._major

  @property
  def email(self):
    return self._email