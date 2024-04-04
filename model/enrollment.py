import pymysql

class Enrollment:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS enrollment (
      id INT AUTO_INCREMENT,
      student_id INT NOT NULL,
      course_id INT NOT NULL,
      FOREIGN KEY (student_id) REFERENCES student(id),
      FOREIGN KEY (course_id) REFERENCES course(id),
      UNIQUE KEY(student_id, course_id),
      PRIMARY KEY (id))"""
    self.cur.execute(sql)
    self.db.commit()
    print("connect ok")

  def get_all(self):
    sql = """select e.id, s.number, s.name, c.name, c.professor, c.credit
    from student s
    join enrollment e
    on (s.id = e.student_id)
    	join course c
      on(c.id = e.course_id)"""
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result

  def add(self,dto):
    sql = "insert ignore into enrollment(student_id, course_id) values({0}, {1});".format(dto.student_id, dto.course_id)
    self.cur.execute(sql)
    self.db.commit()

  def cancel (self, id):
    sql = "delete from enrollment where id = {0}".format(id)
    self.cur.execute(sql)
    self.db.commit()