FROM debian:12

WORKDIR /app
COPY . .


RUN apt update
RUN apt install -y python3 python3-pip

RUN pip3 install -r requirements.txt --break-system-packages

EXPOSE 80

CMD ["gunicorn", "app:app", "-w", "2", "-b", "0.0.0.0:80", "--log-file=-", "--access-logfile=-", "--keep-alive=0"]
