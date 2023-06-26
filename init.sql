# This is the DDL used to create the table and database. 
CREATE DATABASE testdb;
CREATE USER test_user WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE testdb to test_user;
GRANT ALL PRIVILEGES ON TABLE test_table TO test_user;
GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON test_table TO test_user;

\c testdb
DROP TABLE test_table;
CREATE TABLE IF NOT EXISTS test_table (
  "Day"                          DATE,
"Customer ID"                  INTEGER,
"Campaign ID"                   INTEGER,
"Campaign"                     VARCHAR(128),
"Campaign state"               VARCHAR(128),
"Campaign serving status"      VARCHAR(128),
"Clicks"                        INTEGER,
"Start date"                   DATE,
"End date"                     DATE,
"Budget"                        INTEGER,
"Budget ID"                     INTEGER,
"Budget explicitly shared"       BOOLEAN,
"Label IDs"                    VARCHAR(128),
"Labels"                       VARCHAR(128),
"Invalid clicks"                INTEGER,
"Conversions"                 float8,
"Conv. rate"                   VARCHAR(128),
"CTR"                          VARCHAR(128),
"Cost"                          INTEGER,
"Impressions"                   INTEGER,
"Search Lost IS (rank)"        VARCHAR(128),
"Avg. position"               float8,
"Interaction Rate"             VARCHAR(128),
"Interactions"                  INTEGER
);


