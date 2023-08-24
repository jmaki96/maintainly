FROM python:3.10
COPY /src /var/code
COPY /requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["flask", "--app", "/var/code/app", "run", "--host", "0.0.0.0"]