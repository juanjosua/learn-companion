import sqlite3

class Database:
	def __init__(self, name):
		"""Create connection to the database"""
		self.db_name = '{}.db'.format(name)

		print("opened database successfully!")

	
	def create(self, name):
		"""Create new table in database"""
		conn = sqlite3.connect(self.db_name)
		conn.execute('''CREATE TABLE {}
	         (ID 			INTEGER PRIMARY KEY     AUTOINCREMENT,
	         WORD           TEXT    			NOT NULL,
	         MEANING        TEXT     			NOT NULL,
	         DEFINITION     TEXT);'''.format(name))
		conn.close()

		print("Table created successfully!")


	def insert(self, name, word, meaning, definition=None):
		conn = sqlite3.connect(self.db_name)
		conn.execute("INSERT INTO {} (WORD, MEANING, DEFINITION) \
		      VALUES ({}, {}, {})".format(name, word, meaning, definition));
		conn.commit()
		conn.close()

		print("Records created successfully!")


	def read(self, name):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.execute("SELECT id, word, meaning, definition from {}".format(name))
		for row in cursor:
		   print("ID = ", row[0])
		   print("WORD = ", row[1])
		   print("MEANING = ", row[2])
		   print("DEFINITION = ", row[3], "\n")
		conn.close()

		print("Operation done successfully!")


	def update(self, name, column, value, key, key_value):
		conn = sqlite3.connect(self.db_name)
		conn.execute("UPDATE {} set {} = {} where {} = {}".format(name, column, value, key, key_value))
		conn.commit()
		conn.close()

		print("Total number of rows updated :", conn.total_changes)


	def delete(self, name, key, key_value):
		conn = sqlite3.connect(self.db_name)
		conn.execute("DELETE from {} where {} = {};".format(name, key, key_value))
		conn.commit()
		conn.close()

		print("Total number of rows deleted :", conn.total_changes)


	def truncate(self, name):
		conn = sqlite3.connect(self.db_name)
		conn.execute("DELETE FROM {};".format(name.upper()))
		conn.execute("VACUUM;")
		conn.commit()
		conn.close()

		print("Operation done successfully!")


	def drop(self, name):
		conn = sqlite3.connect(self.db_name)
		conn.execute("DROP TABLE {};".format(name))
		conn.commit()
		conn.close()

		print("Tabel {} dropped successfully!".format(name))
		
