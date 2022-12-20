-- creates a atabase with usa states
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa; -- create the database

CREATE TABLE
    IF NOT EXISTS states (
        id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(256)
        ); -- Create a table
