echo Deleting deployWorkerNode job
kubectl delete job deploy-worker-node

echo Deploying a worker node
echo Node: $1
export WORKER=$1
kubectl create -f ../jobs/deployWorkerNode.yaml
