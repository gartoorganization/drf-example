FROM python:3.5

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
ENV DJANGODIR=/django

RUN mkdir $DJANGODIR
WORKDIR $DJANGODIR

COPY requirements.txt $DJANGODIR/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y gettext && apt-get clean && rm -rf /var/lib/apt/lists/*