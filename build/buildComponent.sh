COMPONENT=$1
VERSION=1.4

echo Building component $COMPONENT at version $VERSION

cd ../src/$COMPONENT

IMAGE=patrocinio/icp-scaling-$COMPONENT:$VERSION
docker build --build-arg version=$VERSION -t $IMAGE .

