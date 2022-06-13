import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Projeto_TCC

logs_collection = database.get_collection("logs")

def logs_helper(log) -> dict:
    return {
        "id": str(log["_id"]),
        "FlowID": log["FlowID"],
    }

# Retrieve all logs present in the database
async def retrieve_logs():
    logs = []
    async for logs in logs_collection.find():
        logs.append(logs_helper(logs))
    return logs

async def add_logs_data(logs_data: dict) -> dict:
    logs = await logs_collection.insert_one(logs_data)
    new_log = await logs_collection.find_one({"_id": logs.inserted_id})
    return logs_helper(new_log)

async def retrieve_log(id: str) -> dict:
    logs = await logs_collection.find_one({"_id": ObjectId(id)})
    if logs:
        return logs_helper(logs)

async def update_logs(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    log = await logs_collection.find_one({"_id": ObjectId(id)})
    if log:
        updated_log = await logs_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_log:
            return True
        return False
    
async def delete_log(id: str):
    log = await logs_collection.find_one({"_id": ObjectId(id)})
    if log:
        await logs_collection.delete_one({"_id": ObjectId(id)})
        return True