-- create the database hntn_0d_usa and the table cities
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE cities (
    id INT, AUTO_INCREMENT, NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (state_id) REFERENCES states(id)
    ); -- Creates a cities table
