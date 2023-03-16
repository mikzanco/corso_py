# Introduzione Pythone/MySQL
# installare i drivere mysql py: pip install mysql-connector-python ------------ fatto.
# import e test
# creare una connesione

import mysql.connector

# prepariamo una connessione d'esempio
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YES"
)

print(db)