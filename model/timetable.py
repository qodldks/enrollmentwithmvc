import pymysql

class Timetable:
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='1234', db='posts')
    self.cur = self.db.cursor()