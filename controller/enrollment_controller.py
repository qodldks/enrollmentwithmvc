from flask import jsonify, render_template, request, redirect, url_for, Blueprint
from service.enrollment_service import EnrollmentService
from service.course_service import CourseService
from service.student_service import StudentService
from util.dto import EnrollmentFormDTO

enrollment_blueprint = Blueprint('enrollment', __name__)
enrollment_service = EnrollmentService()
course_service = CourseService()
student_service = StudentService()

@enrollment_blueprint.route('/enrollment_management')
def enrollment_management():
  courses = course_service.get_all()
  students = student_service.get_all()
  enrollments = enrollment_service.get_all()
  print(students)
  return render_template('enrollment_management.html', enrollments = enrollments, courses = courses, students = students)

@enrollment_blueprint.route('/register_enrollment',methods=['POST'])
def register_enrollment():
  dto = EnrollmentFormDTO(student_id = request.form['student_id'],
                          course_id = request.form['course_id'])
  enrollment_service.add(dto)
  return redirect(url_for('enrollment.enrollment_management'))

@enrollment_blueprint.route('/cancel_enrollment', methods=['POST'])
def cancel_enrollment():
  id = request.form['enrollment_id']
  enrollment_service.cancel(id)
  return redirect(url_for('enrollment.enrollment_management'))

@enrollment_blueprint.route('/api/enrollment_list',methods=['GET','POST'])
def enrollment_list():
  enrollments = enrollment_service.get_all()
  return jsonify(enrollments)