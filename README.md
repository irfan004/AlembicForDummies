
# 🏗️ Database Evolution: SQLAlchemy & Alembic Migrations

---

## 📌 Project Overview

This project serves as a hands-on laboratory for mastering **Database Migrations** using Python.  
In modern software engineering—especially when building **Cache Servers**—managing database schema changes **without data loss** is a critical skill.

This repository demonstrates a **Code-First Database Design** approach, simulating the evolution of a production-grade user database from simple tables to advanced schema management using migrations.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **ORM:** SQLAlchemy  
- **Migration Tool:** Alembic  
- **Database:** PostgreSQL (pgAdmin 4)  
- **Environment:** Windows 11 / VS Code  

---

## 🚀 Getting Started

### 1️⃣ Installation

Clone the repository and set up a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install sqlalchemy alembic psycopg2
````

---

### 2️⃣ Configuration

Update the `sqlalchemy.url` in **alembic.ini** with your PostgreSQL credentials:

```ini
sqlalchemy.url = postgresql://postgres:YOUR_PASSWORD@localhost:5432/alembic_test
```

---

### 3️⃣ Initialize the Database

Run the initial migration to upgrade the database to the latest version:

```powershell
alembic upgrade head
```

---

## 📈 Database Evolution Roadmap

This project tracks database schema changes across multiple phases:

### **Phase 1**

* Basic `user` table setup
* Columns: `id`, `name`

### **Phase 2**

* Feature expansion
* Added columns: `email`, `phone_number`

### **Phase 3**

* Column refactoring
* Safely renamed `name` → `full_name`
* Manual migration editing to **preserve existing data**

### **Phase 4**

* Schema synchronization
* Used **Alembic Autogenerate** via `env.py` integration

---

## 📜 Alembic Cheat Sheet

| Command                                    | Description                         |
| ------------------------------------------ | ----------------------------------- |
| `alembic init alembic`                     | Initialize migration environment    |
| `alembic revision -m "msg"`                | Create a manual migration           |
| `alembic revision --autogenerate -m "msg"` | Auto-generate migration from models |
| `alembic upgrade head`                     | Apply all migrations                |
| `alembic downgrade -1`                     | Roll back last migration            |
| `alembic history`                          | View full migration history         |

---

## 💡 Key Learnings

* **Data Integrity:**
  Safely renamed columns using `op.alter_column()` instead of dropping and recreating columns.

* **Safe Rollbacks:**
  Implemented `downgrade()` logic to recover from failed deployments or schema errors.

* **Version Control for Databases:**
  Learned how the `alembic_version` table functions as **Git for databases**.

* **Automation:**
  Configured `env.py` to connect SQLAlchemy `Base.metadata` with Alembic for seamless autogeneration.

---

## 📬 Connect with Me

**Irfan Siddiqui**
Technology & Research Intern
AI / ML Enthusiast

