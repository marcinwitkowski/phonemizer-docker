FROM ubuntu:20.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /phonemizer

EXPOSE 5000

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        festival \
        festvox-us1 \
        festlex-cmu \
        festlex-poslex \
        espeak-ng \
        git \
        mbrola \
        mbrola-fr1 \
        python3 \
        python3-pip && \
    apt-get clean

RUN pip install Flask
RUN pip install pytest
RUN ln -s /usr/bin/python3 /usr/bin/python
COPY . /phonemizer

RUN cd /phonemizer && \
    python3 setup.py install && \
    phonemize --version && \
    python3 -m pytest -v test

CMD ["python3", "app.py"]

