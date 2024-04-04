from flask import render_template, request, redirect, url_for, Blueprint
from service.course_service import CourseService
from service.student_service import StudentService
from util.dto import EnrollmentFormDTO