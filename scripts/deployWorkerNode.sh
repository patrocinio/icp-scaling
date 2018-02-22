#!/bin/bash
set -x
echo Deleting deployWorkerNode job
kubectl delete job deploy-worker-node

echo Deploying a worker node
echo Worker node: $1
export WORKER=$1

CONFIG_MAP=worker-node

kubectl delete configmap $CONFIG_MAP
kubectl create configmap $CONFIG_MAP --from-literal=worker=$WORKER

kubectl create -f ../jobs/deployWorkerNode.yaml
