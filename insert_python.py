import MySQLdb
import random
from datetime import datetime

db = MySQLdb.connect("localhost","tuananh","abc13579","wordpress")
cursor = db.cursor()
sql = "INSERT INTO sensors (temp, hum, time) VALUES (%s, %s, %s)"
val = (int(random.randint(20,40)), random.randint(60,80),datetime.now())
cursor.execute(sql, val)
db.commit()