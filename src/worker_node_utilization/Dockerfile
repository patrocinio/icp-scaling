FROM ubuntu:latest

WORKDIR /usr/src/app

COPY src/ /usr/src/app
RUN apt-get update
RUN apt install -y python3 
RUN apt install -y curl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

RUN apt install -y jq 


CMD ["python3", "top_worker_nodes.py"]