from elasticsearch import Elasticsearch

# Create an Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Define the index name
index_name = "flickrphotos"




# Define the mapping for Elasticsearch index
mapping = { "mappings": {
"properties": {
"id": {"type": "text"},
"userid": {"type": "text"},
"title": {"type": "text"},
"tags": {"type": "text"},
"latitude": {"type": "double"},
"longitude": {"type": "double"},
"views": {"type": "integer"},
"date_taken": {"type": "date","format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
"date_uploaded": {"type": "date","format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
"accuracy": {"type": "short"},
"flickr_secret": {"type": "keyword"},
"flickr_server": {"type": "keyword"},
"flickr_farm": {"type": "keyword"},
"x": {"type": "double"},
"y": {"type": "double"},
"z": {"type": "double"},
"location" : {"type" : "geo_point"}
}
}
}
# Create the Elasticsearch index with the specified mapping of my data
es.indices.create(index=index_name, body=mapping)
