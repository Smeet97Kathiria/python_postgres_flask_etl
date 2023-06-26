# python_postgres_flask_etl
This repository contains code for an ETL web application developed using python, flask and using postgres as a database. 

# What does this web application do ? 
-> The web application reads a delimited file, cleans and processes the data, stores it in a PostgreSQL database, and displays the results in an HTML table. The application  also save the cleaned data to a new gzipped CSV file.


# How to Run the application 
In order to start the application, make sure all the required libraries are installed which are mentioned in requirements.txt. 

After step 1 is complete, run server.py flask application. 

init.sql file contains all the DDl statements used to create the database and table. 

                 +--------------+
                 |  Delimited   |
                 |     File     |
                 +------+-------+
                        |
                        |
                        v
                 +------+-------+
                 |              |
                 | Data Cleaning|
                 |  and Processing
                 |              |
                 +------+-------+
                        |
                        |
                        v
                 +------+-------+
                 |              |
                 | PostgreSQL  |
                 |   Database   |
                 |              |
                 +------+-------+
                        |
                        |
                        v
                 +------+-------+
                 |              |
                 | HTML         |
                 | Interface    |
                 | (HTML Table) |
                 |              |
                 +------+-------+
                        |
                        |
                        v
                 +------+-------+
                 |              |
                 | Gzipped CSV  |
                 |    File      |
                 |              |
                 +--------------+

