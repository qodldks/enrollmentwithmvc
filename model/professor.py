import pymysql

class Professor:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS professor (
      id INT AUTO_INCREMENT,
      name VARCHAR(45) NOT NULL,
      major VARCHAR(45) NOT NULL,
      email VARCHAR(45) NOT NULL,
      PRIMARY KEY (id))"""
    self.cur.execute(sql)
    self.db.commit()

  def get_all(self):
    sql="select * from professor;"
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result

  def add(self,dto):
    sql = """insert into professor(name,major,email) values('{0}','{1}','{2}')""".format(dto.name, dto.major, dto.email)
    self.cur.execute(sql)
    self.db.commit()