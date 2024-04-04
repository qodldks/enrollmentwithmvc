import pymysql

class Course:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS course (
      id INT AUTO_INCREMENT,
      name VARCHAR(45) NOT NULL,
      professor VARCHAR(45) NOT NULL,
      credit INT NOT NULL,
      PRIMARY KEY (id))"""
    self.cur.execute(sql)
    self.db.commit()
    print("connect ok")

  def get_all(self):
    sql = "select * from course;"
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result

  def add(self,dto):
    sql = "insert into course(name, professor, credit) values('{0}', '{1}', {2});".format(dto.name, dto.professor, dto.credit)
    self.cur.execute(sql)
    self.db.commit()

  def select_by_name(self,dto):
    sql = "select * from course where name = '{0}';".format(dto.name)
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result