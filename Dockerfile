FROM python:3.7.13-alpine3.16
WORKDIR /app
RUN apk update && apk add gcc libc-dev
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r ./requirements.txt
COPY main.py ./main.py
CMD ["python", "main.py"]
