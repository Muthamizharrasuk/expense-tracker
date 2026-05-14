from database.mongo import budgets_collection
from bson import ObjectId

async def insert_budget(budget_data):
    result = await budgets_collection.insert_one(budget_data)
    return {"id": str(result.inserted_id)}

async def find_all_budgets():
    result = await budgets_collection.find().to_list(100)
    for budget in result:
        budget["_id"] = str(budget["_id"])
    return result

async def find_one_budget(budget_id):
    result = await budgets_collection.find_one({"_id": ObjectId(budget_id)})
    if result:
        result["_id"] = str(result["_id"])
    return result

async def update_budget(budget_id, update_data):
    result = await budgets_collection.update_one({"_id": ObjectId(budget_id)}, {"$set": update_data})
    return {"modified_count": result.modified_count}
async def delete_budget(budget_id):
    result = await budgets_collection.delete_one({"_id": ObjectId(budget_id)})
    return {"deleted_count": result.deleted_count}