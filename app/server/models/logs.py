from typing import Optional

from pydantic import BaseModel, Field

class LogsSchema(BaseModel):
    SrcPort: int = Field(...) 
    DstPort: int = Field(...)
    TotFwdPkts: int = Field(...)
    FwdPktLenMax: float = Field(...)
    FwdPktLenMin: float = Field(...)
    FwdPktLenMean: float = Field(...)
    FwdPktLenStd: float = Field(...)
    FlowIATMean: float = Field(...)
    FlowIATStd: float = Field(...)
    FlowIATMax: float = Field(...)
    FlowIATMin: float = Field(...)
    FwdIATTot: float = Field(...)
    FwdIATMean: float = Field(...)
    FwdIATStd: float = Field(...)
    FwdIATMax: float = Field(...)
    FwdIATMin: float = Field(...)
    FwdPktss: float = Field(...)
    SYNFlagCnt: int = Field(...)
    RSTFlagCnt: int = Field(...)
    PSHFlagCnt: int = Field(...)
    ACKFlagCnt: int = Field(...)
    CWEFlagCount: int = Field(...)
    ECEFlagCnt: int = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "SrcPort": 4504,
                "DstPort": 80,
                "TotFwdPkts": 29,
                "FwdPktLenMax": 86.0,
                "FwdPktLenMin": 0.0,
                "FwdPktLenMean": 2.9655172413793096,
                "FwdPktLenStd": 15.969799083226464,
                "FlowIATMean": 55206.41666666666,
                "FlowIATStd": 195478.31665363663,
                "FlowIATMax": 1566821.0,
                "FlowIATMin": 167.0,
                "FwdIATTot": 3735347.0,
                "FwdIATMean": 133405.25,
                "FwdIATStd": 341775.6887123293,
                "FwdIATMax": 1805015.0,
                "FwdIATMin": 167.0,
                "FwdPktss": 7.295850774190399,
                "SYNFlagCnt": 1,
                "RSTFlagCnt": 0,
                "PSHFlagCnt": 0,
                "ACKFlagCnt": 0,
                "CWEFlagCount": 0,
                "ECEFlagCnt": 0
            }
        }

class UpdateLogsModel(BaseModel):
    SrcPort: Optional[int] 
    DstPort: Optional[int]
    TotFwdPkts: Optional[int]
    FwdPktLenMax: Optional[float]
    FwdPktLenMin: Optional[float]
    FwdPktLenMean: Optional[float]
    FwdPktLenStd: Optional[float]
    FlowIATMean: Optional[float]
    FlowIATStd: Optional[float]
    FlowIATMax: Optional[float]
    FlowIATMin: Optional[float]
    FwdIATTot: Optional[float]
    FwdIATMean: Optional[float]
    FwdIATStd: Optional[float]
    FwdIATMax: Optional[float]
    FwdIATMin: Optional[float]
    FwdPktss: Optional[float]
    SYNFlagCnt: Optional[int]
    RSTFlagCnt: Optional[int]
    PSHFlagCnt: Optional[int]
    ACKFlagCnt: Optional[int]
    CWEFlagCount: Optional[int]
    ECEFlagCnt: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "SrcPort": 4504,
                "DstPort": 80,
                "TotFwdPkts": 29,
                "FwdPktLenMax": 86.0,
                "FwdPktLenMin": 0.0,
                "FwdPktLenMean": 2.9655172413793096,
                "FwdPktLenStd": 15.969799083226464,
                "FlowIATMean": 55206.41666666666,
                "FlowIATStd": 195478.31665363663,
                "FlowIATMax": 1566821.0,
                "FlowIATMin": 167.0,
                "FwdIATTot": 3735347.0,
                "FwdIATMean": 133405.25,
                "FwdIATStd": 341775.6887123293,
                "FwdIATMax": 1805015.0,
                "FwdIATMin": 167.0,
                "FwdPktss": 7.295850774190399,
                "SYNFlagCnt": 1,
                "RSTFlagCnt": 0,
                "PSHFlagCnt": 0,
                "ACKFlagCnt": 0,
                "CWEFlagCount": 0,
                "ECEFlagCnt": 0
            }
        }

def ResponseModelLogs(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModelLogs(error, code, message):
    return {"error": error, "code": code, "message": message}