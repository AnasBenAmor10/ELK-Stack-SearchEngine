#!/bin/bash


. /opt/bitnami/scripts/liblog.sh

# Run the setup script
info "************************************ Starting Elasticsearch setup ************************************"
/opt/bitnami/scripts/elasticsearch/setup.sh 
info "************************************ Elasticsearch setup finished! ************************************"

# Run the default script script
info ""
/opt/bitnami/scripts/elasticsearch/run.sh &

# Wait for the Elasticsearch to start
info "************************************ Waiting for Elasticsearch to start ************************************"
while true; do
    curl -s http://localhost:9200 && break
    sleep 1
done

# Execute the Python script
info "************************************ Executing create_index_elastic  ************************************"

python3 /usr/share/elasticsearch/scripts/create_index.py

info "************************************ create_index_elastic executed successfully ************************************"

# Keep the container running
tail -f /dev/null