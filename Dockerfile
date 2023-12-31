FROM python:3.10
COPY ./src /var/code/src
COPY ./static /var/code/static
COPY ./templates /var/code/templates
COPY /requirements.txt /requirements.txt
RUN pip install -r requirements.txt
# CMD ["flask", "--app", "/var/code/app", "run", "--host", "0.0.0.0"]
WORKDIR /var/code
CMD ["gunicorn", "--reload", "-w", "4", "-b", "0.0.0.0", "src.wsgi:app"]