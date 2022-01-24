from dataclasses import dataclass
from typing import List, Any

@dataclass
class AirflowConn:
    conn_id: str
    conn_type: str
    host: str
    port: int
    user: str
    password: str


class DAGFactory:
    """ A DAG factory, based on the concrete class and manifest file
    it generates  airflow dag file, airflow variable and airflow connection object"""

    def create_airflow_dag_file(self) -> None:
        """creates a dag file based on the class and manifest provided. Need to add other helper methods to parse the ingestor objects.
        Uses pythonOperator to call the python methods and builds series of tasks in a DAG"""
        pass

    def create_airflow_variables(self) -> List[Any]:
        """based on the inputs in manifests and class, creates a List of variables.
         eg. mongodb: conn_id, """
        pass

    def create_airflow_connection(self) -> AirflowConn:
        """retuns information about the airflow connection"""
        pass


