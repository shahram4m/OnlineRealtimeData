FROM python:3.8
LABEL MAINTIANER="SHAHRAM dOCKER | ZCFCO.IR"

ENV PYTHONNONEBUFFRED 1

RUN mkdir /elements
WORKDIR /elements

COPY . /elements

ADD requirements/requirements.txt /elements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["gunicorn", "--chdir", "elements", "--bind", ":8000", "elements.wsgi:application"]

