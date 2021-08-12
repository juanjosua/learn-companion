from database.database import Database

db = Database("parrot.db")
db.drop("ENGLISH")
db.create("ENGLISH")
db.insert("ENGLISH", "love", "cinta")