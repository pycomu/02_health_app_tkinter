import sqlite3


def connect():
    return sqlite3.connect("health_app.db")

   
def store_account(connection, account_name, account_pin, account_email):
     with connection:
        connection.execute("INSERT INTO account (account_name, account_pin, account_email) VALUES (?, ?, ?)", (account_name, account_pin, account_email))           # arguments(query, tuple of values)
        

'''def read_table(connection):
    with connection:
        return connection.execute().fetchall()'''

