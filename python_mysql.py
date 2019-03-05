import MySQLdb

db = MySQLdb.connect("localhost","tuananh","abc13579","wordpress")
cursor = db.cursor()
sql = """create table sensors(
    id int(10) primary key auto_increment,
    temp int(3) not null,
    hum int(3) not null,
    time datetime not null
)"""
cursor.execute(sql)
db.close()