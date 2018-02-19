echo Deleting deployWorkerNode job
kubectl delete job deploy-worker-node

echo Deploying a worker node
kubectl create -f ../jobs/deployWorkerNode.yaml
