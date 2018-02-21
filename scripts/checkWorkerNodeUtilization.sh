export MEM_THRESHOLD=$1
echo Memory thresold: $1
python3 ../src/worker_node_utilization/top_worker_nodes.py 
