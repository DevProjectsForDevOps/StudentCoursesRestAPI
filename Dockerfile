FROM python:3.7-alpine
LABEL author=KHAJA
LABEL blog=directdevops.blog
ARG HOME_DIR='/studentcourses'
ADD . $HOME_DIR
ENV MYSQL_USERNAME='directdevops'
ENV MYSQL_PASSWORD='directdevops'
ENV MYSQL_SERVER='localhost'
ENV MYSQL_SERVER_PORT='3306'
ENV MYSQL_DATABASE='test'
EXPOSE 8080
WORKDIR $HOME_DIR
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]