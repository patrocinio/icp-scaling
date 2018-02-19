nodes=$(./find_worker_nodes.sh)

echo Worker nodes: $nodes

memory=$(kubectl top nodes | grep $nodes | awk '{print $5}')

echo Memory: $memory
