FROM python:3

COPY . /app

WORKDIR /app

RUN pip3 install flask

ENTRYPOINT ["python"]

CMD ["counter-flask.py"]