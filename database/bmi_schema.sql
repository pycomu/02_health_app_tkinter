CREATE DATABASE bmi;
CREATE TABLE account ( account_id INTEGER PRIMARY KEY,
                       account_name VARCHAR(20), account_email TEXT,
                       account_pin text);
                       
CREATE TABLE user ( user_id INTEGER PRIMARY KEY ,
                    user_name VARCHAR(20), user_gender TEXT,
                    user_dob INTEGER);
                    
CREATE TABLE log_file ( log_id INTEGER PRIMARY KEY,
                        entry_time TIMESTAMP, height FLOAT,
                        weight FLOAT, age INTEGER,
                        bmi FLOAT);