from flask import render_template, request, redirect, url_for, Blueprint
from service.course_service import CourseService
from util.dto import CourseFormDTO

course_blueprint = Blueprint('course', __name__)
course_service = CourseService()

@course_blueprint.route('/')
def home():
  return render_template('index.html')

@course_blueprint.route('/course_management')
def course_management():
  courses = course_service.get_all()
  return render_template('course_management.html', courses = courses)

@course_blueprint.route('/register_course', methods = ['GET','POST'])
def register_course():
  dto = CourseFormDTO(name = request.form['name'],
                      professor = request.form['professor'],
                      credit = int(request.form['credit']))
  course_service.add(dto)
  return redirect(url_for('course.course_management'))