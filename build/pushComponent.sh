COMPONENT=$1
VERSION=1.4

IMAGE=patrocinio/icp-scaling-$COMPONENT:$VERSION

echo Pushing component $COMPONENT as latest version
LATEST=patrocinio/icp-scaling-$COMPONENT:latest
docker tag $IMAGE $LATEST
docker push $LATEST

echo Pushing component $COMPONENT as version $VERSION
docker tag $IMAGE $IMAGE
docker push $IMAGE
