''' Detailed Code Explanation -> Imports necessary libraries such as gzip, pandas, and psycopg2.

Establishes a connection to a PostgreSQL database using psycopg2.

Opens and reads a gzipped CSV file, 'example_report.csv.gz', using the gzip library.

Reads the contents of the gzipped CSV file into a Pandas DataFrame with specified options, such as compression, header, separator, quote character, and error handling.

Prints the total number of rows in the DataFrame.

Writes the contents of the DataFrame to a new gzipped CSV file, 'transform_data.csv.gz', with specified options such as not including the index and using gzip compression.

Truncates (empties) the 'test_table' in the database using an SQL statement and psycopg2 cursor.

Defines a function insertIntoTable that takes three arguments: a database connection, a DataFrame, and a table name. This function does the following:
a. Converts the DataFrame into a list of tuples.
b. Constructs an SQL INSERT statement using the DataFrame columns and table name.
c. Tries to execute the SQL INSERT statement using psycopg2's extras.execute_values() method, which efficiently inserts multiple rows at once.
d. If successful, the function prints a message indicating successful data insertion. If there's an error, it prints the error message, performs a rollback, and returns 1.

Calls the insertIntoTable function to insert the data from the DataFrame into the 'test_table' in the database.

Executes an SQL SELECT statement to count the number of rows in the 'test_table' and prints the result. ''' 

import gzip
import pandas as pd
import psycopg2
import psycopg2.extras as extras
import os


conn = psycopg2.connect("postgresql://test_user:test@localhost/testdb")
cur = conn.cursor()
a_file = gzip.open("example_report.csv.gz", "rb")
contents = a_file.read()
df = pd.read_csv('example_report.csv.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False)

print("There are total {0} rows in the dataframe".format(df.shape[0]))

df.to_csv("transform_data.csv.gz", 
           index=False, 
           compression="gzip")


truncate_statement = 'TRUNCATE TABLE test_table CASCADE;'
cur.execute(truncate_statement)

def insertIntoTable(conn,df, table):
        """
        Using cursor.executemany() to insert the dataframe
        """
        # Create a list of tupples from the dataframe values
        tuples = list(set([tuple(x) for x in df.to_numpy()]))
    
        # Comma-separated dataframe columns
        cols = ', '.join('"' + item + '"' for item in list(df.columns))
        
        tpls = [tuple(x) for x in df.to_numpy()]
        
        # SQL query to execute
        sql = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = conn.cursor()
        try:
            extras.execute_values(cursor, sql, tpls)
            print("Data inserted using execute_values() successfully..")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            return 1
        
insertIntoTable(conn,df,"test_table")

cur.execute("""
    select count(*) from test_table
   ;
""");
for row in cur:
    print(row)


