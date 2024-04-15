from flask import render_template, request, redirect, url_for, Blueprint
from service.timetable_service import TimetableService
# from util.dto import TimetableFormDTO

timetable_blueprint = Blueprint('timetable', __name__)
timetable_service = TimetableService()

@timetable_blueprint.route('/timetable_management',methods=['GET','POST'])
def timetable_management():
  return render_template('timetable_management.html')