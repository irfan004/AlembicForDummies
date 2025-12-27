# 🏗️ Database Evolution: SQLAlchemy & Alembic Migrations



## 📌 Project Overview
This project serves as a hands-on laboratory for mastering **Database Migrations** using Python. In modern software engineering—especially when building **Cache Servers** or **AI/ML Pipelines**—managing database schema changes without losing data is a critical skill. 

This repository demonstrates the **"Code-First"** approach to database management, simulating the evolution of a production-grade user database from simple tables to complex AI-ready structures.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **ORM:** SQLAlchemy (Object Relational Mapper)
* **Migration Tool:** Alembic
* **Database:** PostgreSQL (pgAdmin 4)
* **Environment:** Windows 11 / VS Code

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and set up your virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install sqlalchemy alembic psycopg2 pgvector
2. ConfigurationUpdate the sqlalchemy.url in alembic.ini with your PostgreSQL credentials:Ini, TOMLsqlalchemy.url = postgresql://postgres:YOUR_PASSWORD@localhost:5432/alembic_test
3. Initialize the DatabaseRun the initial migration to reach the "Head" (latest version):PowerShellalembic upgrade head
📈 Database Evolution RoadmapThis project tracks the following schema milestones:Phase 1: Basic User Table (id, name).Phase 2: Feature Expansion (Added email and bio).Phase 3: Column Refactoring (Safe rename of name to full_name via manual script editing).Phase 4: Advanced Data Types (Integration of JSON for settings and Vector for ML embeddings).📜 Alembic Cheat SheetCommandActionalembic init alembicInitialize migration environment.alembic revision --autogenerate -m "msg"Generate a script by comparing models vs database.alembic upgrade headApply all pending changes to the DB.alembic downgrade -1Rollback the last migration (Undo).alembic currentCheck which version the DB is currently on.alembic history --verboseView the full "Git-like" history of migrations.💡 Key LearningsData Integrity: Learned how to manually edit migration scripts to rename columns using op.alter_column instead of dropping them, preventing data loss.Safety Hooks: Utilized downgrade logic to safely revert changes during failed deployments or schema errors.Extensibility: Integrated pgvector to support AI/ML requirements, enabling the storage of high-dimensional embeddings for similarity search.Automation: Configured env.py to bridge SQLAlchemy Base.metadata with Alembic for seamless autogeneration of migration scripts.📬 Connect with MeIrfan Siddiqui Technology & Research Intern | AI/ML Enthusiast
