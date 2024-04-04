from model.professor import Professor

class ProfessorService:
  def __init__(self):
    self.professor = Professor()

  def get_all(self):
    return [{'id':s[0], 'name':s[1], 'major':s[2], 'email':s[3],} for s in self.professor.get_all()]

  def add(self,dto):
    return self.professor.add(dto)