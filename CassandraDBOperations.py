
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
from logger1 import App_Logger






class cassandraDBManagement:
    """
                This class shall be used for the DB operations in Cassandra.

                Written By: Tejas Jay (TJ)
                Version: 1.0
                Revisions: None

            """
    def __init__(self, path, user_id, secure_key, key_space, table_name):
            self.path = path
            self.user_id = user_id
            self.secure_key = secure_key
            self.key_space = key_space
            self.table_name = table_name
            self.logging = App_Logger()




    def cassandra_connection(self):
        """
        Method Name: cassandra_connection
        Description: This method is used to connect to the cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the cassandra_connection method of cassandraDBManagement class')
        try:
            cloud_config = {'secure_connect_bundle': self.path}
            auth_provider = PlainTextAuthProvider(self.user_id, self.secure_key)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            return session
        except Exception as e:
            self.logging.log('Unsuccessful in executing cassandra_connection method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e





    def isconnectionestablished(self):
        """
        Method Name: isconnectionestablished
        Description: This method is used to check if the connection to the cassandra database is established.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the isconnectionestablished method of cassandraDBManagement class')
        try:
            if self.cassandra_connection():
                return True
        except Exception as e:
            self.logging.log('Unsuccessful in executing isconnectionestablished method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e




    def get_key_space(self):
        """
        Method Name: get_key_space
        Description: This method is used to connect to the key_space of the cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the get_key_space method of cassandraDBManagement class')
        try:
            session = self.cassandra_connection()
            row = session.execute("use {}".format(self.key_space))
            return row
        except Exception as e:
            self.logging.log('Unsuccessful in executing get_key_space method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e




    def create_table(self):
        """
        Method Name: create_table
        Description: This method is used to create a table in cassandra database.
        Output: creates table
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the create_table method of cassandraDBManagement class')
        try:
            session = self.cassandra_connection()
            row = session.execute("CREATE TABLE IF NOT EXISTS {}.{table}(ID text PRIMARY KEY, product_name text , product_searched text, Price text, offer_details text,discount_percent text, EMI text, rating text, comment text, customer_name text, review_age text);".format(self.key_space, table=self.table_name)).one()
            return row
        except Exception as e:
            self.logging.log('In exception block of create_table method of cassandraDBManagement class: error message: '+ str(e))
            raise e





    def insert_in_table(self, result):
        """
        Method Name: insert_in_table
        Description: This method is used to insert rows into the table in cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the insert_in_table method of cassandraDBManagement class')
        try:
            session = self.cassandra_connection()
            session.execute("insert into {}.{table} (ID,product_name,product_searched,Price,offer_details,discount_percent,EMI,rating,comment,customer_name,review_age) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);".format(self.key_space, table=self.table_name), result)
            return "Success"
        except Exception as e:
            self.logging.log('Unsuccessful in executing insert_in_table method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e





    def findAllRecords(self):
        """
        Method Name: findAllRecords
        Description: This method is used to get all data from the table in cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the findAllRecords method of cassandraDBManagement class')
        all_records = []
        try:
            session = self.cassandra_connection()
            ss = session.execute("select * from  {}.{table}  ;".format(self.key_space, table=self.table_name))
            for i in ss:
                all_records.append(i)
            return all_records
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing findAllRecords method of the cassandraDBManagement class: error message is: ' + str(
                    e))
            raise e





    def deleteRecords(self):
        """
        Method Name: deleteRecords
        Description: This method is used to delete all the data from the table in cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the deleteRecords method of cassandraDBManagement class')
        try:
            session = self.cassandra_connection()
            session.execute("TRUNCATE {}.{table};".format(self.key_space, table=self.table_name))
        except Exception as e:
            self.logging.log('Unsuccessful in executing deleteRecords method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e





    def findfirstRecord(self, productname):
        """
        Method Name: findfirstRecord
        Description: This method is used to find the first data from the table in cassandra database.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the findfirstRecord method of cassandraDBManagement class')
        try:
            session = self.cassandra_connection()
            first_record = []
            ss = session.execute("select * from {}.{table} WHERE productname= '{product}' LIMIT 1 ALLOW FILTERING;".format(self.key_space,product=productname,table=self.table_name))
            for i in ss:
                first_record.append(i)
                return first_record
        except Exception as e:
            self.logging.log('Unsuccessful in executing findfirstRecord method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e




    def getDataFrame(self):
        """
        Method Name: getDataFrame
        Description: This method is used to convert the records in the table into a dataframe.
        Output: None
        On Failure: Raise Exception

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getDataFrame method of cassandraDBManagement class')
        try:
            dataframe = pd.DataFrame(self.findAllRecords())
            return dataframe
        except Exception as e:
            self.logging.log('Unsuccessful in executing getDataFrame method of the cassandraDBManagement class: error message is: ' + str(e))
            raise e