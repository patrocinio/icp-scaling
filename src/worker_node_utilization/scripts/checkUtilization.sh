bx pr login -a https://10.0.0.1:8443 --skip-ssl-validation -u admin -p admin -c id-icp-account
bx pr cluster-config mycluster

python3 top_worker_nodes.py

