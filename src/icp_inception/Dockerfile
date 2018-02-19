FROM ibmcom/icp-inception:2.1.0.1
WORKDIR /installer/cluster
ARG version

COPY cluster.zip /installer/cluster
RUN unzip -o cluster.zip
