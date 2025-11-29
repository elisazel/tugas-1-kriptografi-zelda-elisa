import mysql.connector

def run_setup():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="paramadaksa"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_payroll")
    conn.close()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="paramadaksa",
        database="db_payroll"
    )
    cursor = conn.cursor()
    
    sql_query = """
    CREATE TABLE IF NOT EXISTS karyawan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(100),
        jabatan VARCHAR(50),
        gaji_encrypted VARCHAR(255)
    )
    """
    
    cursor.execute(sql_query)
    conn.commit()
    conn.close()