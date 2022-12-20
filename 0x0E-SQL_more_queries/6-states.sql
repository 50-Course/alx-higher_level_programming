-- creates a atabase with usa states
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa; -- create the database
CREATE TABLE
    IF NOT EXISTS states (
        id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
        name VARCHAR(256) NOT NULL
        ); -- Create a table
