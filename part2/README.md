Part-2 Solution directory/files structure. 

From DataIngestor which is an abastract base class derive concrete class MongoDBIngestor.

- **airflow**
   - **dags**: dags folder which will contain all the dag files created by dag factory
   - **plugins**: dagfactory will copy all the class files from `source`
   - `dag_factory.py` : DAGFactory will create all the dag files by using the source concrete classes and their mapping.py
                        Implementation will basically copy a dag template file in which it will call `execute` method defined in 
                        `source`.`mongodb`.`main` from pythonOperator
     
   - `_dag_template_file.py`: predfined configuration of dag, with pythonoperator task.DAGFactory will create tasks 
                              based on the configuration in the manifest.py file

- **source**
    - **mongodb**
        - `manifest.yaml` : holds information about source and target and their mapping, adding source table is very easy 
                          and maintainable
        - `main.py` : execute method which will be called inside pythonOperator created by DAGFactory
        - `mongodb_ingestor.py` : concrete class derived from DataIngestor abstract class
    - `data_ingestor.py`: abstract class can be used as a blueprint to add any other source in future
    
- **tests**
    - `ingestion_tests.py` : unit tests which will test the implementation of concrete methods of MongodbIngestor, 
                            in future more tests can be added to tests other soure classes
    

    
