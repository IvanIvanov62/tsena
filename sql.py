import sqlite3

db = sqlite3.connect('shop.db', check_same_thread=False)
myCursor = db.cursor()


def db_start():
    myCursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INT, 
        nameid TEXT,
        sms TEXT) 
    """)

def delit():
    myCursor.execute(f"DELITE FROM users WHERE id = '{chislo}' ")
    db.commit()
    print('запись удалена')