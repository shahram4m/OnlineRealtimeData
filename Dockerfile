FROM python:3.8
LABEL MAINTIANER="SHAHRAM dOCKER | ZCFCO.IR"

ENV ELEMENTS_SERVICE=/home/app/elements

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir -p $ELEMENTS_SERVICE
RUN mkdir -p $ELEMENTS_SERVICE/static

# where the code lives
WORKDIR $ELEMENTS_SERVICE

# install psycopg2 dependencies
#RUN apk update \
#    && apk add --virtual build-deps gcc python3-dev musl-dev \
#    && apk add postgresql-dev gcc python3-dev musl-dev \
#    && apk del build-deps \
#    && apk --no-cache add musl-dev linux-headers g++

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $ELEMENTS_SERVICE


ADD requirements/requirements.txt $ELEMENTS_SERVICE
RUN pip install -r requirements.txt


CMD ["gunicorn", "--chdir", "elements", "--bind", ":8000", "elements.wsgi:application"]

