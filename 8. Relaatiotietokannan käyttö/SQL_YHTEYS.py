import mysql.connector

def sql_yhteys()->mysql.connector.connect:
    yhteys = {
             'host': '127.0.0.1',
             'port': '3306',
             'database': 'flight_game',
             'user': 'root',
             'password': 'root',
             'autocommit': True,
            }

    return mysql.connector.connect(**yhteys)
