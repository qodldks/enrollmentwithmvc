from flask import render_template, request, redirect, url_for, Blueprint
from service.course_service import CourseService
from service.professor_service import ProfessorService
from service.lecture_service import LectureService
from util.dto import LectureFormDTO

lecture_blueprint = Blueprint('lecture', __name__)
lecture_service = LectureService()
professor_service = ProfessorService()
course_service = CourseService()

@lecture_blueprint.route('/lecture_management')
def lecture_management():
  lectures = lecture_service.get_all()
  professors = professor_service.get_all()
  courses = course_service.get_all()
  return render_template('lecture_management.html', lectures=lectures, professors=professors, courses=courses)


@lecture_blueprint.route('/register_lecture',methods=['GET','POST'])
def register_lecture():
  dto = LectureFormDTO(professor_id = request.form['professor_id'],
                       course_id = request.form['course_id'],
                       day = request.form['day'],
                       start_time =  request.form['start_time'],
                       end_time = request.form['end_time'])
  lecture_service.add(dto)
  return redirect(url_for('lecture.lecture_management'))

@lecture_blueprint.route('/cancel_lecture',methods=['GET','POST'])
def cancel_lecture():
  id = request.form['id']
  lecture_service.delete(id)
  return redirect(url_for('lecture.lecture_management'))