import pymysql

class Student:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS student (
      id INT AUTO_INCREMENT,
      number INT NOT NULL,
      name VARCHAR(45) NOT NULL,
      gender VARCHAR(45) NOT NULL,
      PRIMARY KEY (id))"""
    self.cur.execute(sql)
    self.db.commit()
    print("connect ok")

  def get_all(self):
    sql = "select * from student;"
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result

  def get(self,number):
    sql = "select * from student where number = {0}".format(number)
    self.cur.execute(sql)
    result = self.cur.fetchone()
    return result

  def add(self,dto):
    sql = "insert into student(number, name, gender) values({0}, '{1}', '{2}');".format(dto.number, dto.name, dto.gender)
    self.cur.execute(sql)
    self.db.commit()