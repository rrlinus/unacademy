from flask import Blueprint, jsonify, request, session
from bson.json_util import dumps
import datetime
from ..util.authenticator import Authenticator
from . import main
from ..models import Courses, Subject, Syllabus, Client, Video

@main.route('/courses')
def findCourses():
    courses = Courses.query.filter_by().all()
    res = {}
    for course in courses:
        res[course.course_id] = course.course_name;
    return jsonify(res)


@main.route('/syllabus/<course_name>')
@main.route('/syllabus')
def findAllSyllabus(course_name = ""):
    if course_name:
        courses = Courses.query.filter_by(course_name=course_name).all()
    else:
        courses = Courses.query.filter_by().all()
    res = {}
    for course in courses:
        syllabuses = Syllabus.query.filter_by(course_id = course.course_id).all()
        l = []
        for syllabus in syllabuses:
            subject = Subject.query.filter_by(subject_id = syllabus.subject_id).first()
            l.append(subject.subject_name)
        res[course.course_name] = l
    return jsonify(res);


@main.route('/courses/videos/')
@Authenticator.authenticate
def get_videos():
    user_id = session['root_uid']
    courses = Client.query.filter_by(user_id=user_id).all()
    res = {}
    course_res = []
    map_courses = {}
    for course in courses:
        course_name = (Courses.query.filter_by(course_id=course.course_id).first()).course_name
        syllabuses = Syllabus.query.filter_by(course_id=course.course_id).all()
        course_details = []
        map_subject = {}
        for syllabus in syllabuses:
            subject_name = (Subject.query.filter_by(subject_id=syllabus.subject_id).first()).subject_name;
            videos = Video.query.filter_by(subject_id=syllabus.subject_id).all()
            video_details = []
            for video in videos:
                video_details.append(
                    {
                        'url': video.video_url,
                        # 'teacher_id': video.teacher_id,
                        'subject_id': video.subject_id,
                        'video_id': video.video_id
                    }
                )
            map_subject[subject_name] = video_details
        map_courses[course_name] = map_subject
    return jsonify(map_courses)














