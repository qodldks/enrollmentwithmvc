from flask import Flask
from controller.course_controller import course_blueprint
from controller.student_controller import student_blueprint
from controller.enrollment_controller import enrollment_blueprint
from controller.professor_controller import professor_blueprint

app = Flask(__name__)

app.register_blueprint(student_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(enrollment_blueprint)

if __name__ == '__main__':
  app.run(debug=True)