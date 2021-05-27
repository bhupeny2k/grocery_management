import datetime
import mysql.connector

def get_sql_connection():
  print("Opening mysql connection")
  cnx = mysql.connector.connect(host="localhost", user='root', password='', database='grocery_store')
  return cnx
