import sqlite3

db = sqlite3.connect("DataBase.db")
cursor = db.cursor()

class MethodsDB:
    
    def createTable(nameTable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {nameTable}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                LastName TEXT NOT NULL )""")
        db.commit()
    
    def showAllIDs(nameTable):
        cursor.execute(f"SELECT id FROM {nameTable}")
        return cursor.fetchall()

    def InsertObject(nameTable, name, lastName):
        cursor.execute(f"INSERT INTO {nameTable} (Name, LastName) VALUES(?,?)", (name, lastName))
        db.commit()
    
    def InsertObjects(nameTable, ListAll):
        cursor.executemany(f"""INSERT INTO {nameTable} (name, LastName) VALUES(?,?)""", ListAll)
        db.commit()
    
    def ReadObject(nameTable, id):
        cursor.execute(f"SELECT * FROM {nameTable} WHERE id = {id}")
        return cursor.fetchall()
    
    def ReadObjects(nameTable):
        cursor.execute(f"SELECT * FROM {nameTable}")
        return cursor.fetchall()

    def UpdateObject(NameTable, Id, nameNew, lastNameNew):
        cursor.execute(f'''UPDATE {NameTable} SET Name = ?, LastName = ? WHERE id = ? ''', 
                    (nameNew, lastNameNew, Id))
        db.commit()
    
    def RemoveObject(NameTable, IdOld):
        cursor.execute(F"DELETE FROM {NameTable} WHERE id = ?", (IdOld,))
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = ?", (NameTable,))
        db.commit()