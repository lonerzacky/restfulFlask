FROM python:2.7
ADD . /restfulFlask
WORKDIR /restfulFlask
EXPOSE 4000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
