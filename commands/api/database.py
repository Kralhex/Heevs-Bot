from mysql import connector

from secret import DATABASE

db = connector.connect(
	host = DATABASE["host"],
	port = DATABASE["port"],
	user = DATABASE["user"],
	password = DATABASE["password"],
	database = DATABASE["database"]
)

db_cursor = db.cursor(dictionary = True)