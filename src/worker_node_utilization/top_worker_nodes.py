import subprocess

MEM_THRESOLD = 10

available_nodes = ["10.0.0.2", "10.0.0.4", "10.0.0.5", "10.0.0.6"]

def find_worker_nodes ():
	print ("Finding worker nodes...")
	cmd='kubectl get no -o json | \
		jq \'.items[].metadata | select (.labels.role != "master") | select (.labels.proxy != "true") | .name\' | \
		tr -d \'"\' | tr -d \'\n\''

	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	output = ps.communicate()[0]

	workers = set()
	worker = output.decode('utf-8')
	workers.add (worker)
	return workers

def top_nodes (workers):
	with subprocess.Popen(["kubectl","top","nodes"], stdout=subprocess.PIPE) as proc:
		lines =  proc.stdout.read().splitlines()
		for line in lines:
			columns = line.split()
			node = columns[0].decode('utf-8')

			if node in workers:
				print (line.decode('utf-8'))
				return int(columns[4].decode('utf-8').strip("%"))

def find_available_node (workers):
	for node in available_nodes:
		if node not in workers:
			return node
	return None

def deploy_worker_node (avail):
	print ("TBD")	


workers = find_worker_nodes();
print (workers)
memory = top_nodes (workers);
print ("Memory: " + str(memory));

if memory > MEM_THRESOLD :
	print ("Need to deploy a new node")
	avail = find_available_node(workers)
	print ("Available " + avail)