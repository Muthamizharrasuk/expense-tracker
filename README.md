# Expense Tracker with Budget Alerts

This project is an Expense Tracker application designed to help you manage budgets, track expenses, and get alerts when spending exceeds your budget limits. It follows a three-tier architecture with a React frontend, FastAPI backend, and MongoDB data store.

## Tech Stack
- Frontend: React.js + Vite
- Backend: FastAPI (Python)
- Database: MongoDB
- API client: Axios

## Features
- Create, read, update, and delete budgets
- Create, read, update, and delete expenses
- Track spending against budgets
- Budget alerts when spending exceeds the budget limit
- Separate frontend and backend layers following best practices

## Project Structure

```
expense-tracker/
├── backend/
│   ├── main.py
│   ├── controllers/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── utils/
└── frontend/
    ├── public/
    └── src/
        ├── components/
        ├── pages/
        ├── services/
        └── styles/
```

- `backend/` contains the API entrypoint, business logic controllers, route definitions, database connection, and schemas.
- `frontend/` contains the React application, UI components, and service layer for API calls.

## How to Run Locally

### Backend
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Activate the Python virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```
5. Open API docs:
   - `http://127.0.0.1:8000/docs`

### Frontend
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend app:
   ```bash
   npm run dev
   ```
4. Open the app:
   - `http://localhost:5173`

## API Documentation
Once the backend is running, open:
- `http://127.0.0.1:8000/docs`

## Architecture
This application uses three-tier architecture:
- Presentation Layer: React frontend renders UI and communicates with backend APIs.
- Business Logic Layer: FastAPI handles validation, requests, and budget/expense rules.
- Data Access Layer: MongoDB stores budgets and expenses, and the backend reads/writes this data.

## Learning Notes
- Build your UI components in `frontend/src/` and keep API calls in `frontend/src/services/`.
- Keep validation and business rules in backend controllers.
- Use Pydantic models to enforce request/response data shapes.
- MongoDB stores records and returns document IDs automatically.

## Next Steps
- Add budget alert badges in the UI
- Improve expense list filtering and sorting
- Add user authentication
- Containerize the app with Docker
