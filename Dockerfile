FROM ubuntu:16.04
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install mutt -y
RUN chmod +x jota-cert-checker.sh
RUN mkfifo /var/spool/postfix/public/pickup
RUN service postfix restart
RUN apt-get install python3
RUN apt-get install python3-pip
RUN pip3 install python-crontab
CMD ["python3", "/usr/src/app/main.py"]
#CMD ["/bin/sh","/usr/src/app/jota-cert-checker.sh -f sitelist -o html -m durandelegba@gmail.com"]
#CMD ["sh jota-cert-checker.sh -f sitelist -o html -m durandelegba@gmail.com"]