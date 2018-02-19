import subprocess

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
				return columns[4]


workers = find_worker_nodes();
print (workers)
memory = top_nodes (workers);
print (memory.decode('utf-8'));