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
        "SrcPort": log["Src Port"],
        "DstPort": log["Dst Port"], 
        "TotFwdPkts": log["Tot Fwd Pkts"],
        "FwdPktLenMax": log["Fwd Pkt Len Max"],
        "FwdPktLenMin": log["Fwd Pkt Len Min"],
        "FwdPktLenMean": log["Fwd Pkt Len Mean"],
        "FwdPktLenStd": log["Fwd Pkt Len Std"],
        "FlowIATMean": log["Flow IAT Mean"],
        "FlowIATStd": log["Flow IAT Std"],
        "FlowIATMax": log["Flow IAT Max"],
        "FlowIATMin": log["Flow IAT Min"],
        "FwdIATTot": log["Fwd IAT Tot"],
        "FwdIATMean": log["Fwd IAT Mean"],
        "FwdIATStd": log["Fwd IAT Std"],
        "FwdIATMax": log["Fwd IAT Max"],
        "FwdIATMin": log["Fwd IAT Min"],
        "FwdPktss": log["Fwd Pkts/s"],
        "SYNFlagCnt": log["SYN Flag Cnt"],
        "RSTFlagCnt": log["RST Flag Cnt"],
        "PSHFlagCnt": log["PSH Flag Cnt"],
        "ACKFlagCnt": log["ACK Flag Cnt"],
        "CWEFlagCount": log["CWE Flag Count"],
        "ECEFlagCnt": log["ECE Flag Cnt"],
    }

def logs_helper(log) -> dict:
    return {
        "id": str(log["_id"]),
        "SrcPort": log["SrcPort"],
        "DstPort": log["DstPort"], 
        "TotFwdPkts": log["TotFwdPkts"],
        "FwdPktLenMax": log["FwdPktLenMax"],
        "FwdPktLenMin": log["FwdPktLenMin"],
        "FwdPktLenMean": log["FwdPktLenMean"],
        "FwdPktLenStd": log["FwdPktLenStd"],
        "FlowIATMean": log["FlowIATMean"],
        "FlowIATStd": log["FlowIATStd"],
        "FlowIATMax": log["FlowIATMax"],
        "FlowIATMin": log["FlowIATMin"],
        "FwdIATTot": log["FwdIATTot"],
        "FwdIATMean": log["FwdIATMean"],
        "FwdIATStd": log["FwdIATStd"],
        "FwdIATMax": log["FwdIATMax"],
        "FwdIATMin": log["FwdIATMin"],
        "FwdPktss": log["FwdPktss"],
        "SYNFlagCnt": log["SYNFlagCnt"],
        "RSTFlagCnt": log["RSTFlagCnt"],
        "PSHFlagCnt": log["PSHFlagCnt"],
        "ACKFlagCnt": log["ACKFlagCnt"],
        "CWEFlagCount": log["CWEFlagCount"],
        "ECEFlagCnt": log["ECEFlagCnt"],
    }

def getlogin_helper(login) -> dict:
    return {
        "id": str(login["_id"]),
        "email": login["email"],
        "senha": login["senha"],
    }

# Retrieve all logs present in the database
async def retrieve_logs():
    someLogs = []
    async for logs in logs_collection.find():
        someLogs.append(getlogs_helper(logs))
    return someLogs

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
    logins = []
    async for login in login_collection.find():
        logins.append(getlogin_helper(login))
    return logins


async def retrieve_login(id: str) -> dict:
    login = await login_collection.find_one({"_id": ObjectId(id)})
    if login:
        return getlogin_helper(login)

async def add_login_data(login_data: dict) -> dict:
    login = await login_collection.insert_one(login_data)
    new_login = await login_collection.find_one({"_id": login.inserted_id})
    return getlogin_helper(new_login)

async def update_logins(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    login = await login_collection.find_one({"_id": ObjectId(id)})
    if login:
        updated_login = await login_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_login:
            return True
        return False

async def delete_login(id: str):
    login = await login_collection.find_one({"_id": ObjectId(id)})
    if login:
        await login_collection.delete_one({"_id": ObjectId(id)})
        return True