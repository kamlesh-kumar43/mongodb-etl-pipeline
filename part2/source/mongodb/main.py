from assignment4.part2.source.mongodb.mongodb_ingestor import MongoDBIngestor
import logging

logging = logging.basicConfig()


def execute(manifest_file: str, env: str):
    logging.debug("intializing mongodb driver...")
    mongo = MongoDBIngestor(manifest_file, env)

    # stage:1 connection intialization
    mongo_client = mongo.get_source_connection()
    redshift_client = mongo.get_target_connection()

    # stage:2 source data to s3 bucket
    # inside for loop for all the source_target mapping call
    mongo.get_source_data()

    # stage:3 from s3 bucket to redshift
    mongo.load_data_to_target()
