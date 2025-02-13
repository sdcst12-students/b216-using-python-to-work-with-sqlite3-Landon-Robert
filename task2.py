#!python
import sqlite3
"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()
cursor.execute('delete from petInfo') 
query = """
create table if not exists buyers (
    name tinytext,
    email tinytext,
    phoneNumber int,
    ID tinyint,
    address tinytext,
    balance tinytext);
"""
cursor.execute(query)
data = [

]
print("----------------------")
for i in data:
    query = f"insert into buyers (name,email,phoneNumber,ID,address,balance) values ('{i[0]}','{i[1]}','{i[2]}',{i[3]},'{i[4]}',{i[5]});"
    cursor.execute(query)
query = "select * from buyers"
cursor.execute(query)
connection.commit()
result = cursor.fetchall()
print(result)
for i in result:
    print(i)