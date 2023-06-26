# What does this application do ? 
-> The primary purpose of this application is to extract and transform gzipped file and save the data into a table in postgres database. After the table is populated with data from gzipped file, A flask application is ran which reads the data from a database using postgres client and renders it onto a webpage in a table format. 


# How to Run the application 
In order to start the application, make sure all the required libraries are installed which are mentioned in requirements.txt. 

After step 1 is complete, run server.py flask application. 

init.sql file contains all the DDl statements used to create the database and table. 


