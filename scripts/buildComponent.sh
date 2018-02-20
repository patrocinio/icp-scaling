COMPONENT=icp_inception
VERSION=1.1

echo Building component $COMPONENT at version $VERSION

cd ../src/$COMPONENT

IMAGE=patrocinio/icp-scaling-$COMPONENT:$VERSION
docker build --build-arg version=$VERSION -t $IMAGE .

