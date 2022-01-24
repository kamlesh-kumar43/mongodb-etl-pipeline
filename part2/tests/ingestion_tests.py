from pymongo import MongoClient

from assignment4.part2.source.mongodb.mongodb_ingestor import MongoDBIngestor


def mongodb_connection_test():
    """asserts if the connection establishes successful"""
    mongodb_obj = MongoDBIngestor("/assignment4/part2/source/mongodb/manifest.yaml")
    assert isinstance(mongodb_obj.get_source_connection(), MongoClient), "mongoDB connection failed"

def get_data_from_mongodb_collection_test():
    """asserts if the data fetching is working"""
    mongodb_obj = MongoDBIngestor("/assignment4/part2/source/mongodb/manifest.yaml")
    data = mongodb_obj.get_source_data(limit=1)
    assert isinstance(data, dict), "return object is not a valid json"

def data_from_collection_test():
    "load predefined data in one collection"
    mongodb_obj = MongoDBIngestor("/assignment4/part2/source/mongodb/manifest.yaml")
    assert "json_data_from_collection" == { "preloaded dummy data to assert against" }


def loaded_data_in_redshift_test():
    assert "get data from redshift table" == "get data loaded in mongodb collection"
