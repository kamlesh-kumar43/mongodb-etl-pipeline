from abc import ABC, abstractmethod


class DataIngestor(ABC):
    """Abstract class for data ingestion from different sources"""

    @abstractmethod
    def get_source_connection(self, *args, **kwargs):
        """method to create connection object returns client object"""
        pass

    @abstractmethod
    def get_source_data(self, *args, **kwargs):
        """get data from source, return type may be json object, list object or csv file"""
        pass

    @abstractmethod
    def get_target_connection(self, *args, **kwargs):
        """get connection object of the target object"""
        pass

    @abstractmethod
    def load_data_to_target(self, *args, **kwargs):
        """store data to the target"""
        pass

    @abstractmethod
    def close_connection(self, *args, **kwargs):
        """close any active session, connection or client"""
        pass
