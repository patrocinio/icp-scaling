FROM ibmcom/icp-inception:2.1.0.1
WORKDIR /installer
ARG version

COPY cluster.zip /installer/cluster
RUN cd /installer/cluster && unzip -o cluster.zip
