from flask import render_template, request, redirect, url_for, Blueprint
from service.student_service import StudentService
from util.dto import StudentFormDTO

student_blueprint = Blueprint('student', __name__)
student_service = StudentService()

@student_blueprint.route('/student_management')
def student_management():
  students = student_service.get_all()
  return render_template('student_management.html', students = students)

@student_blueprint.route('/register_student', methods=['POST'])
def register_student():
  dto = StudentFormDTO(number = request.form['number'],
                       name = request.form['name'],
                       gender = request.form['gender'])
  student_service.add(dto)
  return redirect(url_for('student.student_management'))