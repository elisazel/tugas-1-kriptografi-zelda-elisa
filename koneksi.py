import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="paramadaksa",
        database="db_payroll"
    )