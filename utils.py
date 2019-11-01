from flask_restplus import reqparse, fields, Api


def get_course_parser():
    """
    This method returns the course parse
    :return:
    """
    course_parser = reqparse.RequestParser()
    course_parser.add_argument('id', type=int)
    course_parser.add_argument('name')
    course_parser.add_argument('faculty')
    course_parser.add_argument('duration', type=int)
    return course_parser


def get_course_model(api):
    """

    :type api: Api
    """
    course_model = api.model('CourseModel', {
        'id': fields.Integer,
        'name': fields.String,
        'faculty': fields.String,
        'duration': fields.Integer
    })
    return course_model
