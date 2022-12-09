from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    """
    Sample Student Table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    email = db.Column(db.String(length=256), unique=True, nullable=False)
    phone = db.Column(db.String(length=11), nullable=False)

    def __repr__(self) -> str:
        return "<Student id {}>".format(self.id)


class Course(db.Model):
    """
    Sample Course Table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    faculty = db.Column(db.String(length=100), nullable=False)
    duration = db.Column(db.Integer)

    def __repr__(self) -> str:
        return "<Course id {}>".format(self.id)


student_courses = db.Table('studentcourses',
                           db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                           db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
                           )


class Institute(db.Model):
    """
    Sample Institute Table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    email = db.Column(db.String(length=256), unique=True, nullable=False)
    phone = db.Column(db.String(length=11), nullable=False)

    def __repr__(self) -> str:
        return "<Institute id {}>".format(self.id)