FROM ubuntu

RUN apt-get update
RUN apt-get install -y supervisor && \
    apt-get install -y python3-pip
RUN pip3 install motor && \
    pip3 install tornado

COPY . /usr/
WORKDIR /usr/

EXPOSE 80
CMD /usr/bin/supervisord -c supervisord.conf