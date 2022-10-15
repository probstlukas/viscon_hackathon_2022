FROM python

#COPY requirements.txt /
COPY . /app
RUN pip3 install -r ./app/requirements.txt

#WORKDIR /app

EXPOSE 8080

#CMD [ "sh gunicorn --chdir app main:app -b 0.0.0.0:8080" ]
ENTRYPOINT ["./app/gunicorn.sh"]