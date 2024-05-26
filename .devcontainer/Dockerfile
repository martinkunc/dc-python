FROM alpine


RUN apk add \
    wget \
    bash \
    shadow \
    python3 \
    py3-pip \
    git \
    python3-tkinter \
    xvfb

    

RUN chsh -s /bin/bash root

RUN python3 -m venv .venv && source .venv/bin/activate
