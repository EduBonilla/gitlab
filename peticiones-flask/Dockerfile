FROM python:3

COPY . /app

WORKDIR /app

RUN pip3 install flask

RUN pip3 install requests

RUN pip3 install visdom

ENTRYPOINT ["python"]

CMD ["enviar-peticion-flask.py"]