from database.mongo import expenses_collection
from bson import ObjectId

async def insert_expense(expense_data):
    expense_data["date"] = str(expense_data["date"])
    result = await expenses_collection.insert_one(expense_data)
    return {"id": str(result.inserted_id)}

async def find_all_expenses():
    result = await expenses_collection.find().to_list(100)
    for expense in result:
        expense["_id"] = str(expense["_id"])
    return result

async def find_one_expense(expense_id):
    result = await expenses_collection.find_one({"_id": ObjectId(expense_id)})
    if result:
        result["_id"] = str(result["_id"])
    return result

async def update_expense(expense_id, update_data):
    result = await expenses_collection.update_one({"_id": ObjectId(expense_id)}, {"$set": update_data})
    return {"modified_count": result.modified_count}
async def delete_expense(expense_id):
    result = await expenses_collection.delete_one({"_id": ObjectId(expense_id)})
    return {"deleted_count": result.deleted_count}