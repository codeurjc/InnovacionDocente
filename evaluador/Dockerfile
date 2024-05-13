FROM python:3.12

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY Results.py Results.py

EXPOSE 7860

ENV GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_NAME=0.0.0.0

CMD ["gradio", "app.py"]

# TO BUILD docker build -t evaluador .
# TO RUN   docker run -p 7860:7860 -v $PWD:/usr/src/app evaluador