from flask import Flask
from controller.course_controller import course_blueprint
from controller.student_controller import student_blueprint
from controller.enrollment_controller import enrollment_blueprint
from controller.professor_controller import professor_blueprint
from controller.lecture_controller import lecture_blueprint
from controller.timetable_controller import timetable_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(student_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(lecture_blueprint)
app.register_blueprint(enrollment_blueprint)
app.register_blueprint(timetable_blueprint)

if __name__ == '__main__':
  app.run(debug=True) 