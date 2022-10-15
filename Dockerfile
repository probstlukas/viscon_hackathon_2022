FROM python

COPY requirements.txt /
COPY . /app
RUN pip3 install -r ./requirements.txt

WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]