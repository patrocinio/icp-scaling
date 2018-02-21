echo Deleting cron job
kubectl delete cronjob worker-node-utilization

echo Creating cron job
kubectl create -f ../jobs/workerNodeUtilization.yaml