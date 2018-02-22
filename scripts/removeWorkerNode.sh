echo Removing worker node $1

docker run -e LICENSE=accept --net=host \
patrocinio/icp-scaling-icp_inception:latest \
install -l $1
