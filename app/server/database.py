import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Projeto_TCC

logs_collection = database.get_collection("logs")
login_collection = database.get_collection("login")

def getlogs_helper(log) -> dict:
    return {
        "id": str(log["_id"]),
        "FlowID": log["Flow ID"],
    }

def logs_helper(log) -> dict:
    return {
        "id": str(log["_id"]),
        "FlowID": log["FlowID"],
    }

def getlogin_helper(login) -> dict:
    return {
        "id": str(login["_id"]),
        "email": str(login["email"]),
        "senha": login["senha"],
    }

# Retrieve all logs present in the database
async def retrieve_logs():
    logs = []
    async for logs in logs_collection.find():
        logs.append(getlogs_helper(logs))
    return logs

async def add_logs_data(logs_data: dict) -> dict:
    logs = await logs_collection.insert_one(logs_data)
    new_log = await logs_collection.find_one({"_id": logs.inserted_id})
    return logs_helper(new_log)

async def retrieve_log(id: str) -> dict:
    logs = await logs_collection.find_one({"_id": ObjectId(id)})
    if logs:
        return getlogs_helper(logs)

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

#Login
async def retrieve_logins():
    login = []
    async for login in login_collection.find():
        return getlogin_helper(login)
        # login.append(getlogin_helper(login))


async def retrieve_login(id: str) -> dict:
    login = await login_collection.find_one({"_id": ObjectId(id)})
    if login:
        return getlogin_helper(login)

async def add_login_data(login_data: dict) -> dict:
    login = await login_collection.insert_one(login_data)
    new_login = await login_collection.find_one({"_id": login.inserted_id})
    return getlogin_helper(new_login)