from pymongo import MongoClient
from assignment4.part2.source.data_ingestor import DataIngestor
import pymongo
import yaml
import redshift_connector

class MongoDBIngestor(DataIngestor):

    def __init__(self, manifest_file: str, env: str = "dev", cred_type: str = "FROM_AIRFLOW"):
        self.manifest = yaml.safe_load(open(manifest_file, "r"))
        self.env = env
        self.src_hostname = self.manifest["envs"][self.env]["source"]["hostname"]
        self.src_port = self.manifest["envs"][self.env]["source"]["port"]
        self.src_database = self.manifest["envs"][self.env]["source"]["database"]
        self.cred_type = cred_type
        self.src_username, self.src_password = self._get_credentials("mongodb", self.src_database)
        self.tgt_hostname = self.manifest["envs"][self.env]["target"]["hostname"]
        self.tgt_port = self.manifest["envs"][self.env]["target"]["port"]
        self.tgt_database = self.manifest["envs"][self.env]["target"]["database"]
        self.tgt_username, self.tgt_password = self._get_credentials("redshift", self.tgt_database)
        self.source_target = self.manifest["envs"][self.env]["source_target"]

    def get_source_connection(self, hostname: str, port: int) -> MongoClient:
        return pymongo.MongoClient(hostname,
                                   port,
                                   user=self.src_username,
                                   password=self.src_password)

    def get_target_connection(self):
        return redshift_connector.connect(
            host=self.tgt_hostname,
            database=self.tgt_database,
            user=self.tgt_username,
            password=self.tgt_password
        )

    def get_source_data(self):
        client = self.get_source_connection(self.src_hostname, self.src_port)
        db = client.get_database(self.src_database)
        for collection in self.source_target:
            source_collection, target_table = collection.items()
            self.store_in_s3(self.read_data_from_collection(client, db, source_collection))

    def read_data_from_collection(self, client, db, collection: str):
        """reads data from mongodb collection, fetch all records in json format"""
        pass

    def store_in_s3(self, s3_client):
        """after getting the results from mongodb store in s3 files as .json files"""
        pass

    def load_data_to_target(self):
        """read json data from s3 bucket, intilaizes the redshift client and load data into redshift tables"""
        pass

    def _get_credentials(self, database_type: str, database_name: str):
        if self.cred_type == "FROM_VAULT":
            database_type
            database_name
            # return username from vault, password from vault
            return 'abc', 'xxx'

        if self.cred_type == "FROM_AIRFLOW":
            # return username from airflow conn, password from airflow conn
            return 'pqr', 'yyy'
