from flask import render_template, request, redirect, url_for, Blueprint
from service.professor_service import ProfessorService
from util.dto import ProfessorFormDTO

professor_blueprint = Blueprint('professor', __name__)
professor_service = ProfessorService()

@professor_blueprint.route('/professor_management')
def professor_management():
  professors = professor_service.get_all()
  return render_template('professor_management.html', professors = professors)

@professor_blueprint.route('/register_professor',methods=['POST'])
def register_professor():
  dto = ProfessorFormDTO(name=request.form['name'],
                         major=request.form['major'],
                         email=request.form['email'])
  professor_service.add(dto)
  return redirect(url_for('professor.professor_management'))