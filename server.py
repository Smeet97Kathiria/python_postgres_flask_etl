''' Detaile Code Explanation -> Import necessary libraries and set up the Flask application with a filesystem-based session.

Connect to the PostgreSQL database with psycopg2.

Define the index() function, which renders the index.html template when the user accesses the root path ("/") of the web application.

Define the start() function, which is executed when a POST request is made to the "/start/" path. The function does the following:
a. Reads and parses the gzipped CSV file using Pandas.
b. Writes the parsed data back to a new gzipped CSV file.
c. Truncates the test_table in the database to remove any existing data.
d. Inserts the parsed data into the test_table.
e. Redirects the user to the results page.

Define the results() function, which retrieves data from the test_table in the database, loads it into an HTML table, and renders the table.html template when the user navigates to the "/results" path.

Run the Flask application with a secret key and debug mode enabled. ''' 


from flask import Flask,session,redirect, url_for
from flask import render_template,request
from flask_session import Session
import gzip
import pandas as pd
import psycopg2
import psycopg2.extras as extras
from sqlalchemy import create_engine
import os
app = Flask(__name__)
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=os.urandom(24))
app.config.from_object(__name__)
Session(app)
conn = psycopg2.connect("postgresql://test_user:test@localhost/testdb")
cur = conn.cursor()

@app.route('/')
def index():
    # df = pd.read_csv('transform_data.csv.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False) 
    return render_template('index.html')

@app.route("/start/", methods=['POST'])
def start():
    '''
    Parsing the Data
    '''
    a_file = gzip.open("example_report.csv.gz", "rb")
    contents = a_file.read()
    df = pd.read_csv('example_report.csv.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False)
    
    '''
    Writing the parsed data
    '''
    df.to_csv("transform_data.csv.gz", index=False, compression="gzip")
    truncate_statement = 'TRUNCATE TABLE test_table CASCADE;'
    cur.execute(truncate_statement)
    
    '''
    Saving the parsed data in test_table
    '''
    cols = ', '.join('"' + item + '"' for item in list(df.columns))
    tpls = [tuple(x) for x in df.to_numpy()]
    sql = "INSERT INTO %s(%s) VALUES %%s" % ("test_table", cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, sql, tpls)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1
        
    '''
    Navigating to results page to display saved data in test_table
    '''
    return redirect(url_for('results'))

@app.route('/results')
def results():
    '''
    Getting data from test_table and loading it into html table
    '''
    cols = ['Day', 'Customer ID', 'Campaign ID', 'Campaign', 'Campaign state', 'Campaign serving status', 
            'Clicks','Start date', 'End date', 'Budget', 'Budget ID', 'Budget explicitly shared', 
            'Label IDs', 'Labels', 'Invalid clicks', 'Conversions', 'Conv. rate', 
            'CTR', 'Cost', 'Impressions', 'Search Lost IS (rank)', 'Avg. position', 
            'Interaction Rate', 'Interactions']
    cur.execute("""
                select * from test_table;
                            """);
    tuples = cur.fetchall()
    df = pd.DataFrame(tuples, columns=cols)
    return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)


if __name__ == "__main__":
    app.secret_key = "My Secret key"
    app.run()
    app.run(debug=True)
    
# export FLASK_APP=server.py
# python3 -m flask run --host=0.0.0.0