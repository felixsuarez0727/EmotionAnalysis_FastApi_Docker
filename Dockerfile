FROM python:3.8

# copy requirements file
COPY requirements.txt requirements.txt

# install required packages
RUN apt-get update && apt-get install -y libgirepository1.0-dev libcairo2-dev libcairo2 python3-cairo python3-dev pkg-config
RUN apt-get update && apt-get install -y build-essential libpython3-dev libdbus-1-dev
RUN apt-get update && apt-get install -y uvicorn && pip3 install -r requirements.txt 

# copy application files
COPY ./app /app

EXPOSE 8080
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8080"]
