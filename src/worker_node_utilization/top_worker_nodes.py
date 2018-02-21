import subprocess
import sys

MEM_THRESOLD = 75

available_nodes = ["10.0.0.2", "10.0.0.4", "10.0.0.5", "10.0.0.6"]

def find_worker_nodes ():
	print ("Finding worker nodes...")
	cmd='kubectl get no -o json | \
		jq \'.items[].metadata | select (.labels.role != "master") | select (.labels.proxy != "true") | .name\' | \
		tr -d \'"\''

	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	output = ps.communicate()[0]

	workers = set()
	worker = output.decode('utf-8')
	worker_list = worker.split()
	for w in worker_list:
		print ("worker: " + w)
		workers.add (w)
	return workers

def top_nodes (workers):
	with subprocess.Popen(["kubectl","top","nodes"], stdout=subprocess.PIPE) as proc:
		lines =  proc.stdout.read().splitlines()
		sum = 0
		count = 0
		for line in lines:
			columns = line.split()
			node = columns[0].decode('utf-8')

			if node in workers:
				perc = columns[4].decode('utf-8')
				print (node + ": " + perc);
				mem = int(perc.strip("%"))
				sum += mem
				count += 1

		return sum / count 



def find_available_node (workers):
	for node in available_nodes:
		if node not in workers:
			return node
	return None

def deploy_worker_node (avail):
	print ("Deploying a worker node...")
	with subprocess.Popen(["./deployWorkerNode.sh"], stdout=subprocess.PIPE, 
		shell=True) as proc:
		lines = proc.stdout.read().splitlines()
		for line in lines:
			print (line.decode('utf-8'))

def check_memory_utilization (memory, workers):
	if memory > MEM_THRESOLD :
		print ("Need to deploy a new node")
		avail = find_available_node(workers)
		print ("Available " + avail)
		deploy_worker_node (avail)
	else:
		print ("No need to scale")

workers = find_worker_nodes();
print (workers)
memory = top_nodes (workers);
print ("Memory: " + str(memory));

if len(sys.argv) < 2 or sys.argv[1] != 'check':
	check_memory_utilization (memory, workers);
