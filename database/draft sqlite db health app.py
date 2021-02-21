import sqlite3 # check content of db here https://sqliteonline.com/


conn = sqlite3.connect('./database/health_app.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = 1")

# create table "account"
c.execute("""CREATE TABLE IF NOT EXISTS account ( 
            account_id integer primary key,
            login text not null,
            password text not null
            )""")

# create table "user" ++ foreign key(account_id) REFERENCES account(account_id));""")
c.execute("""CREATE TABLE IF NOT EXISTS user ( 
            user_id integer primary key,
            first_name text not null,
            last_name text not null,
            dateofbith date null,
            gender text          
            )""")

# create table "logfile" foreign key(user_id) REFERENCES user(user_id)
c.execute("""CREATE TABLE IF NOT EXISTS logfile ( 
            logfile_id integer primary key,
            timestamp date,
            weight real,
            height real,
            bmi real
            )""")


