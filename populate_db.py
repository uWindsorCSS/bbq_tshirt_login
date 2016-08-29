import sqlite3
import csv

db = sqlite3.connect("./users.db")

def format_name(name):
    return " ".join(name.split(", ")[::-1])

def get_names_from(csv_filename):
    names = []
    with open(csv_filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for student in reader:
            names.append(format_name(student[0]))
    return names


for name in get_names_from("./students.csv"):
    cur = db.execute("insert into users (name) values (?)", (name,))
    cur.close()

db.commit()
db.close()
