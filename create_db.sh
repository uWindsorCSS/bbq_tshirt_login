echo "setting up structure..."
sqlite3 users.db < schema.sql
echo "populating..."
python ./populate_db.py
echo "done!"
