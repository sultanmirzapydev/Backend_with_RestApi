import mysql.connector as mysql

db = mysql.connect(
	host = 'localhost';
	user = 'root';
	passwd='';
	)

cursor = db.cursor()

