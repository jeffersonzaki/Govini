FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev

RUN pip3 install fuzzywuzzy && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter && \
    pip3 install strings && \
    pip3 install re

WORKDIR /Users/zakijefferson/code/Govini
COPY . .

RUN pip3 install jupyter

WORKDIR /Users/zakijefferson/code/Govini

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
