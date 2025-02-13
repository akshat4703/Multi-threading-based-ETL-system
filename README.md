# ETL Project with Multithreading

## 📌 Project Overview
This project showcases different ETL (Extract, Transform, Load) methods using Python and MySQL. The goal is to compare execution times for three approaches:

1. **One-by-One Transfer** – Transfers data row by row.
2. **Import/Export Using CSV** – Transfers data using a CSV file.
3. **Multithreading** – Uses parallel processing for faster execution.

After execution, the three methods are compared based on execution time using a graph.

---

## 🛠️ Technologies Used
- **Python** (Scripting language)
- **MySQL** (Database)
- **MySQL Connector** (Python library for MySQL)
- **Pandas** (For CSV handling)
- **Threading** (For parallel execution)
- **Matplotlib** (For visualization)

---

## 📁 Project Structure
```
ETL_Project/
│── TransferDataOneByOne.py       # Case 1: One-by-One Transfer
│── TransferDataImportExport.py   # Case 2: Using Import/Export
│── TransferDataMultithreading.py # Case 3: Using Multithreading
│── CompareExecutionTimes.py      # Generates comparison graph
│── config.py                     # Database configuration
│── README.md                     # Project documentation
│── requirements.txt               # Dependencies
```

---

## ⚙️ Setup Instructions
### **1️⃣ Install Required Dependencies**
Ensure you have Python installed. Then, install dependencies:
```sh
pip install mysql-connector-python pandas threading time matplotlib
```

### **2️⃣ Set Up MySQL Database**
Create a database and tables in MySQL:
```sql
CREATE DATABASE etl_db;
USE etl_db;

CREATE TABLE source_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
);

CREATE TABLE destination_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
);
```
Insert sample data:
```sql
INSERT INTO source_table (name, age) VALUES 
('Alice', 25),
('Bob', 30),
('Charlie', 22),
('David', 35);
```

### **3️⃣ Update Database Configuration**
Modify `config.py` or update connection settings directly in each script:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "etl_db",
    "port": 3306
}
```

---

## 🚀 Running the Scripts
### **1️⃣ Case 1: One-by-One Transfer**
```sh
python TransferDataOneByOne.py
```
### **2️⃣ Case 2: Import/Export Using CSV**
```sh
python TransferDataImportExport.py
```
### **3️⃣ Case 3: Multithreading Transfer**
```sh
python TransferDataMultithreading.py
```

### **4️⃣ Compare Execution Times**
After running all three scripts, update `CompareExecutionTimes.py` with execution times and generate a comparison graph:
```sh
python CompareExecutionTimes.py
```

---

## 📊 Expected Results
| ETL Method          | Execution Time (Seconds) |
|---------------------|------------------------|
| One-by-One         | X.XX                    |
| Import/Export      | X.XX                    |
| Multithreading     | X.XX                    |

- **One-by-One Transfer**: Slowest due to row-by-row insertion.
- **Import/Export**: Faster due to batch processing.
- **Multithreading**: Fastest due to parallel execution.

---

## 🏆 Conclusion
This project highlights how different ETL methods perform in data transfer scenarios. It demonstrates the advantages of using multithreading for efficient processing.

🔹 **One-by-One Transfer**: Basic method, slowest.
🔹 **Import/Export**: Medium speed, uses batch operations.
🔹 **Multithreading**: Fastest, due to parallel execution.
