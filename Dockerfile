FROM python

ENV TZ="Europe/Zurich"

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Zurich /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

#COPY requirements.txt /
COPY . /app
RUN pip3 install -r ./app/requirements.txt

#WORKDIR /app

EXPOSE 8080

VOLUME [ "/app/instance/img/" ]

#CMD [ "sh gunicorn --chdir app main:app -b 0.0.0.0:8080" ]
ENTRYPOINT ["./app/gunicorn.sh"]