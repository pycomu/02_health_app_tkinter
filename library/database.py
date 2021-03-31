import sqlite3



insert_into_account_table = "INSERT INTO account (account_name, account_pin, account_email) VALUES (?, ?, ?);"
read_account__table = "SELECT......."


def connect():
    return sqlite3.connect("health_app.db")

   
def store_account(connection, account_name, account_pin, account_email):
     with connection:
        connection.execute(insert_into_account_table, (account_name, account_pin, account_email))           # arguments(query, tuple of values)
        

def read_table(connection):
    with connection:
        return connection.execute(read_account_table).fetchall()

