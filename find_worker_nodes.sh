kubectl get no -o json | \
jq '.items[].metadata | select (.labels.role != "master") | select (.labels.proxy != "true") | .name' |
tr -d '"'