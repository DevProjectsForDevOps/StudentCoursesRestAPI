from flask import Flask, jsonify
import os
import logging
from flask_restplus import Api, Resource, fields, reqparse
from models import db, Course
import utils

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
    os.getenv('MYSQL_USERNAME', 'directdevops'),
    os.getenv('MYSQL_PASSWORD', 'directdevops'),
    os.getenv('MYSQL_SERVER', 'localhost'),
    os.getenv('MYSQL_DATABASE', 'test'))
app.logger.debug("Database URI is {}".format(DATABASE_URI))
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

api = Api(app, version='0.1.1', title='Testing Service', description='Test Service for k8s')

ns = api.namespace('course', description="Courses Namespace")
course_parser = utils.get_course_parser()
course_model = utils.get_course_model(api)


@ns.route("/initialize")
@api.doc()
class Initialize(Resource):
    """
    Initialize Resource
    """

    @api.response(200, 'Success')
    @api.response(500, 'Error with database initialization')
    def get(self):
        """
        This method initializes the database
        :return:
        """
        try:
            app.logger.info("initializing database")
            db.create_all()
            return 'Database Created', 200
        except Exception as e:
            app.logger.error("Following Error occurred {}".format(str(e)))
            return jsonify({"error": e}), 500


@ns.route("/course")
@api.doc()
class Courses(Resource):
    """
    This resource will deal with Courses
    """

    @ns.doc('list course')
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

    @ns.doc(parser=course_parser)
    @ns.response(200, description="success", model=course_model)
    @ns.expect(course_model)
    @ns.marshal_with(course_model)
    def post(self):
        course_from_payload = course_parser.parse_args()
        course = Course(
            id=course_from_payload['id'],
            name=course_from_payload['name'],
            faculty=course_from_payload['faculty'],
            duration=course_from_payload['duration']
        )
        db.session.add(course)
        db.session.commit()
        return course


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=os.getenv('APP_PORT', 8080), debug=True, host="0.0.0.0")
