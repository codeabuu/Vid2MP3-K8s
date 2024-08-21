FROM python:3.10-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev pkg-config\
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

ENV JWT_SECRET=s3cUr3!R@nd0mK3y_2024*Th@tSh0uldN0tBeGuessed!

EXPOSE 5000

CMD ["python3", "server.py"]