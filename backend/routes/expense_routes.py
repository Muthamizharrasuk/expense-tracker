from fastapi import APIRouter
router = APIRouter()
from models.expense_model import ExpenseCreate, ExpenseUpdate
from controllers.expense_controller import insert_expense, find_all_expenses, find_one_expense, update_expense, delete_expense


@router.get("/expenses")
async def get_expenses():
    return await find_all_expenses()

@router.get("/expenses/{expense_id}")
async def get_expense(expense_id: str):
    return await find_one_expense(expense_id)

@router.post("/expenses")
async def create_expense(expense: ExpenseCreate):
    return await insert_expense(expense.model_dump())

@router.put("/expenses/{expense_id}")
async def update_expense_route(expense_id: str, expense: ExpenseUpdate):
    return await update_expense(expense_id, expense.model_dump(exclude_unset=True))
@router.delete("/expenses/{expense_id}")
async def delete_expense_route(expense_id: str):
    return await delete_expense(expense_id)

