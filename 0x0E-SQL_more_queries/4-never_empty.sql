-- Creates the table id_not_null on the server
CREATE TABLE
    IF NOT EXISTS id_not_null (
        id INT DEFAULT 0,
        name VARCHAR(256)
        );
