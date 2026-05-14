from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.expense_routes import router as expense_router
from routes.budget_routes import router as budget_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)
app.include_router(budget_router)

@app.get("/")
async def root():
    return {"message": "Expense Tracker API is running"}