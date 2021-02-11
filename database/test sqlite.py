import sqlite3 

conn = sqlite3.connect('bmi.db')

c = conn.cursor()

# create table "user"
c.execute("""CREATE TABLE IF NOT EXISTS user ( 
            name text,
            weight real,
            height real,
            gender text
            )""")


# def store_sql(value_in): # something wrong here
#     with conn:
#         c.execute("INSERT INTO user VALUES (:name, :weight, :height, :gender)", {'name':value_in.name, 'weight':value_in.weight, 'height':value_in.height, 'gender':value_in.gender})

def store_sql(value_in):
    with conn:
        c.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (value_in))

if __name__ == "__main__":

    name_in = str(input("your name is ? "))
    weight_in = float(input("your weigt in Kg is ? "))
    height_in = float(input("your height in m is ? "))
    gender_in = str(input("your gender is male/female ? "))
    input_user = (name_in, weight_in, height_in, gender_in)
    
    store_sql(input_user)
    
    conn.close()

    # https://www.pythoncentral.io/introduction-to-sqlite-in-python/
    # check content of db here https://sqliteonline.com/
