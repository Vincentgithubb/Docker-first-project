FROM debian:12

COPY app.py requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

WORKDIR /app/

RUN sudo apt update && sudo apt install -y python3 python3-pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "app.py" ]