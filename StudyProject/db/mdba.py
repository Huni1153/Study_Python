import mysql.connector

config = {
    'user' : 'root',
    'password' : '1153',
    'host' : '127.0.0.1',
    'database' : 'pythondb',
    'port' : '3306'
}

def getConn():
    conn = mysql.connector.connect(**config)
    return conn
