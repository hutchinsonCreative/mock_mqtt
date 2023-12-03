FROM python:3.8
WORKDIR /
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD python src/server.py
