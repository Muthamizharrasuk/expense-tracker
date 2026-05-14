from fastapi import APIRouter
router = APIRouter()
from models.budget_model import BudgetCreate, BudgetUpdate
from controllers.budget_controller import find_all_budgets, find_one_budget, insert_budget, update_budget, delete_budget


@router.get("/budgets")
async def get_budgets():
    return await find_all_budgets()

@router.get("/budgets/{budget_id}")
async def get_budget(budget_id: str):
    return await find_one_budget(budget_id)

@router.post("/budgets")
async def create_budget(budget: BudgetCreate):
    return await insert_budget(budget.model_dump())

@router.put("/budgets/{budget_id}")
async def update_budget_route(budget_id: str, budget: BudgetUpdate):
    return await update_budget(budget_id, budget.model_dump(exclude_unset=True))
@router.delete("/budgets/{budget_id}")
async def delete_budget_route(budget_id: str):
    return await delete_budget(budget_id)

