# 🚀 AWS 3-Tier Web Application (Flask + RDS + Load Balancer)

## 📌 Project Overview

This project demonstrates a **3-tier architecture** deployed on AWS using:

* **Frontend** → HTML (EC2)
* **Backend** → Python Flask (EC2)
* **Database** → AWS RDS (MySQL)
* **Load Balancer** → Application Load Balancer (ALB)

The application allows users to:

* Insert data into database
* View stored data

---

## 🏗️ Architecture

Frontend → Load Balancer → Backend → RDS Database

---

## 🛠️ Technologies Used

* AWS EC2
* AWS RDS (MySQL)
* AWS Load Balancer (ALB)
* Python (Flask)
* HTML + JavaScript
* PyMySQL

---

## ⚙️ Setup Steps

### 1️⃣ Launch EC2 Instances

* Create 2 EC2 instances:

  * Frontend Server
  * Backend Server

---

### 2️⃣ Setup Backend (Flask)

Install dependencies:

```bash
sudo yum update -y
sudo yum install python3 -y
pip3 install flask pymysql
```

Create `app.py`:

```python
from flask import Flask
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host="YOUR-RDS-ENDPOINT",
    user="admin",
    password="YOUR-PASSWORD",
    database="appdb"
)

@app.route('/')
def home():
    return "Backend Connected to Database 🚀"

@app.route('/add')
def add():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Disha')")
    connection.commit()
    return "Data Inserted!"

@app.route('/view')
def view():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return str(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

Run backend:

```bash
python3 app.py
```

---

### 3️⃣ Setup RDS Database

* Create MySQL RDS instance
* Allow EC2 access in Security Group

Run:

```sql
CREATE DATABASE appdb;
USE appdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);
```

---

### 4️⃣ Setup Load Balancer

* Create Application Load Balancer
* Add backend EC2 to Target Group
* Listener → HTTP (Port 80)

---

### 5️⃣ Setup Frontend

Create simple HTML page:

```html
<h1>My AWS 3-Tier App 🚀</h1>

<button onclick="addData()">Add Data</button>
<button onclick="viewData()">View Data</button>

<script>
function addData() {
    fetch("http://<LOAD-BALANCER-DNS>/add")
        .then(res => res.text())
        .then(data => alert(data));
}

function viewData() {
    fetch("http://<LOAD-BALANCER-DNS>/view")
        .then(res => res.text())
        .then(data => alert(data));
}
</script>
```

---

## 📸 Project Screenshots

### 🔹 Frontend UI

![Frontend](1_frontend-ui.png)

### 🔹 Backend Running

![Backend](2_backend-running.png)

### 🔹 Database Connected

![Database](3_db-connected.png)

### 🔹 Data Inserted

![Insert](4_data-inserted.png)

---

## ⭐ Final Output (Main Result)

👉 This is the final working system output:

![Final Output](5_final-output.png)

✔ Data is successfully:

* Inserted from frontend
* Processed by backend
* Stored in RDS
* Retrieved via Load Balancer

---

## 🎯 Key Features

* 3-Tier Architecture Implementation
* Real-time Data Insertion
* Load Balancer Integration
* Cloud Deployment using AWS
* Database Connectivity with RDS

---

## 🚀 Conclusion

This project demonstrates how to build and deploy a **scalable cloud-based 3-tier web application** using AWS services.

It highlights:

* Separation of concerns (Frontend, Backend, Database)
* Cloud infrastructure management
* Real-world deployment practices

---

## 👩‍💻 Author

**Disha (AWS Learner 🚀)**

---

## ⭐ Future Improvements

* Add UI design (CSS / React)
* Use Auto Scaling
* Add authentication system
* Deploy using Docker & CI/CD

---
