 
# 🌟 Fullstack AI Mini Solution

Welcome to the **Fullstack AI Mini Solution**! This project is a modern FastAPI backend designed for AI-powered energy prediction, event tracking, and data aggregation. It leverages cutting-edge Python libraries and containerization for seamless local development and deployment.

---

## 🚀 Tech Stack
- **FastAPI**: High-performance Python web framework
- **SQLAlchemy**: ORM for database interactions
- **PostgreSQL**: Robust relational database
- **Docker & Docker Compose**: Containerized development & deployment
- **pytest**: Powerful testing framework
- **Joblib, NumPy**: Machine learning utilities
- **PgAdmin**: Database management UI

---

## 🛠️ Build & Run Locally

### 1. Prerequisites
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Clone the Repository
```sh
git clone https://github.com/DanPhala/fullstack-ai-mini-solution.git
cd fullstack-ai-mini-solution
```

### 3. Build & Start All Services
```sh
docker-compose up --build
```
- **Backend**: http://localhost:8000
- **PgAdmin**: http://localhost:5894 (login: admin@example.com / admin)
- **Postgres**: localhost:6741

### 4. Run Tests
```sh
docker-compose run test
```
Or, locally (requires Python 3.11 & dependencies):
```sh
pip install -r requirements.txt
pytest tests/
```

---

## 🧑‍💻 Development
- Main app entry: `main.py`
- API endpoints: `controllers/`
- Database models: `database/db_models.py`
- ML models: `ML/models/model.pkl`
- Tests: `tests/`

---

## ✨ Features
- Real-time event streaming
- Daily energy aggregation
- ML-powered predictions
- Async database operations
- Full test coverage

---

## 📦 Environment Variables
Set in `docker-compose.yml`:
- `DATABASE_URL`: PostgreSQL connection string
- `MODELS_DIR`: ML model directory

---

## 💡 Quick Start
1. Build & run with Docker Compose
2. Access API docs at: [http://localhost:8000/docs](http://localhost:8000/docs)
3. Explore, test, and extend!

---


