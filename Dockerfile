FROM python:3.6

RUN apt-get -y update \
    && apt-get install -y \
        fonts-font-awesome \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
        libcairo2 \
    && apt-get -y clean

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

RUN apt-get install -y locales locales-all

CMD ["/bin/bash"]
