import pymysql

class Lecture:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()
    sql="""CREATE TABLE IF NOT EXISTS lecture(
		       id INT AUTO_INCREMENT,
		       professor_id INT NOT NULL,
		       course_id INT NOT NULL,
		       day VARCHAR(5) NOT NULL,
		       start_time VARCHAR(45) NOT NULL,
		       end_time VARCHAR(45) NOT NULL,
		       FOREIGN KEY (professor_id) REFERENCES professor(id),
		       FOREIGN KEY (course_id) REFERENCES course(id),
		       PRIMARY KEY (id))"""
    self.cur.execute(sql)
    self.db.commit()

  def get_all(self):
    sql = """select l.id, p.name, p.major, c.name, c.credit, l.day, l.start_time, l.end_time
    				 from lecture l
  					 join professor p
				     on (p.id = l.professor_id)
				     	 join course c
				       on(c.id = l.course_id)"""
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result

  def add(self,dto):
    sql = """insert into lecture(professor_id, course_id, day, start_time, end_time)
    				 values({0},{1},'{2}','{3}','{4}')""".format(dto.professor_id, dto.course_id, dto.day, dto.start_time, dto.end_time)
    self.cur.execute(sql)
    self.db.commit()

  def delete(self,id):
    sql="delete from lecture where id = {0}".format(id)
    self.cur.execute(sql)
    self.db.commit()