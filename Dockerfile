FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev

RUN pip3 install fuzzywuzzy && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter

WORKDIR /Users/zakijefferson/code/Govini
COPY . .

RUN pip3 install jupyter

RUN curl --silent --location https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update 
RUN apt-get install -y apt-utils
RUN apt-get install -y libltdl7
RUN apt-get install -y npm 
RUN apt-get install -y dnsutils
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /Users/zakijefferson/code/Govini

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
