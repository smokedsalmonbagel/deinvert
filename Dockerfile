FROM ubuntu:20.04
ENV TZ=America/New_York
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install  \
    build-essential libsndfile1-dev libliquid-dev automake ffmpeg python3 \
	&& apt-get clean
RUN ldconfig
RUN mkdir /work
WORKDIR /work
COPY ./autogen.sh ./autogen.sh
COPY ./configure.ac ./configure.ac
COPY ./Makefile.am ./Makefile.am
COPY ./README.md ./README.md
RUN mkdir ./src
COPY ./src ./src
RUN chmod u+x /work/autogen.sh  
RUN sh ./autogen.sh && sh ./configure && make
RUN mkdir /work/audio
COPY ./entrypoint.py ./entrypoint.py
ENTRYPOINT ["python3","/work/entrypoint.py"]