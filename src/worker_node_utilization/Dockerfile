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

RUN curl https://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/0.6.5/IBM_Cloud_CLI_0.6.5_amd64.tar.gz > bx.tar.gz

RUN tar xzvf bx.tar.gz

RUN Bluemix_CLI/install_bluemix_cli

COPY plugin/ /tmp

RUN bx plugin install /tmp/icp-linux-amd64

COPY scripts/ /usr/src/app

CMD ["bash", "./checkUtilization.sh"]