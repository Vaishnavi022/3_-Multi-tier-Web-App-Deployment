from flask import Flask
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # Fix CORS issue

# Database connection
connection = pymysql.connect(
    host="mydb.cd48wqmg2qf7.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="YOUR_PASSWORD",  # 🔥 replace this
    database="appdb"
)

# Home route
@app.route('/')
def home():
    return "Backend Connected to Database 🚀"

# Insert data
@app.route('/add')
def add():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Disha')")
    connection.commit()
    return "Data Inserted!"

# View data
@app.route('/view')
def view():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return str(data)

# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)