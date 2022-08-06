FROM python:slim-buster
WORKDIR /app
RUN apt-get update && apt-get install -y git gcc
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r ./requirements.txt
COPY main.py ./main.py
CMD ["python", "main.py"]
