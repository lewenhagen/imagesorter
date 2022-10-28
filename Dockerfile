FROM ubuntu:22.04
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN apt update
RUN apt install -y \
    python3 tree python3-pip \
    libtiff-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev libmagic-dev

RUN pip3 install Pillow python-magic

WORKDIR /app

COPY *.py ./

ENTRYPOINT [ "python3", "/app/main.py" ]
