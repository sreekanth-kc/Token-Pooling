FROM ubuntu:16.04
WORKDIR /app
COPY . /app
RUN apt-get update -y
RUN apt-get dist-upgrade -y
ENV MYSQL_PWD arjun
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
RUN apt-get install mysql-server -y
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python-mysqldb -y
RUN apt-get install python3-dev -y
RUN apt-get install -y python3-pip
RUN apt install python3-venv -y  && python3 -m venv venv && . venv/bin/activate
RUN pip3 --no-cache-dir install -r requirements.txt
RUN apt-get install memcached -y
RUN memcached -u root &
EXPOSE 8083
ENTRYPOINT ["python3"]
CMD ["main.py"]
