from typing import Optional

from pydantic import BaseModel, Field

class LogsSchema(BaseModel):
    SrcPort: str = Field(...) 
    DstPort: str = Field(...)
    TotFwdPkts: str = Field(...)
    FwdPktLenMax: str = Field(...)
    FwdPktLenMin: str = Field(...)
    FwdPktLenMean: str = Field(...)
    FwdPktLenStd: str = Field(...)
    FlowIATMean: str = Field(...)
    FlowIATStd: str = Field(...)
    FlowIATMax: str = Field(...)
    FlowIATMin: str = Field(...)
    FwdIATTot: str = Field(...)
    FwdIATMean: str = Field(...)
    FwdIATStd: str = Field(...)
    FwdIATMax: str = Field(...)
    FwdIATMin: str = Field(...)
    FwdPktss: str = Field(...)
    SYNFlagCnt: str = Field(...)
    RSTFlagCnt: str = Field(...)
    PSHFlagCnt: str = Field(...)
    ACKFlagCnt: str = Field(...)
    CWEFlagCount: str = Field(...)
    ECEFlagCnt: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "Src Port": "4504",
                "Dst Port": "80",
                "Tot Fwd Pkts": "29",
                "Fwd Pkt Len Max": "86.0",
                "Fwd Pkt Len Min": "0.0",
                "Fwd Pkt Len Mean": "2.9655172413793096",
                "Fwd Pkt Len Std": "15.969799083226464",
                "Flow IAT Mean": "55206.41666666666",
                "Flow IAT Std": "195478.31665363663",
                "Flow IAT Max": "1566821.0",
                "Flow IAT Min": "167.0",
                "Fwd IAT Tot": "3735347.0",
                "Fwd IAT Mean": "133405.25",
                "Fwd IAT Std": "341775.6887123293",
                "Fwd IAT Max": "1805015.0",
                "Fwd IAT Min": "167.0",
                "Fwd Pkts/s": "7.295850774190399",
                "SYN Flag Cnt": "1",
                "RST Flag Cnt": "0",
                "PSH Flag Cnt": "0",
                "ACK Flag Cnt": "0",
                "CWE Flag Count": "0",
                "ECE Flag Cnt": "0"
            }
        }

class UpdateLogsModel(BaseModel):
    SrcPort: Optional[str] 
    DstPort: Optional[str]
    TotFwdPkts: Optional[str]
    FwdPktLenMax: Optional[str]
    FwdPktLenMin: Optional[str]
    FwdPktLenMean: Optional[str]
    FwdPktLenStd: Optional[str]
    FlowIATMean: Optional[str]
    FlowIATStd: Optional[str]
    FlowIATMax: Optional[str]
    FlowIATMin: Optional[str]
    FwdIATTot: Optional[str]
    FwdIATMean: Optional[str]
    FwdIATStd: Optional[str]
    FwdIATMax: Optional[str]
    FwdIATMin: Optional[str]
    FwdPktss: Optional[str]
    SYNFlagCnt: Optional[str]
    RSTFlagCnt: Optional[str]
    PSHFlagCnt: Optional[str]
    ACKFlagCnt: Optional[str]
    CWEFlagCount: Optional[str]
    ECEFlagCnt: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Src Port": "4504",
                "Dst Port": "80",
                "Tot Fwd Pkts": "29",
                "Fwd Pkt Len Max": "86.0",
                "Fwd Pkt Len Min": "0.0",
                "Fwd Pkt Len Mean": "2.9655172413793096",
                "Fwd Pkt Len Std": "15.969799083226464",
                "Flow IAT Mean": "55206.41666666666",
                "Flow IAT Std": "195478.31665363663",
                "Flow IAT Max": "1566821.0",
                "Flow IAT Min": "167.0",
                "Fwd IAT Tot": "3735347.0",
                "Fwd IAT Mean": "133405.25",
                "Fwd IAT Std": "341775.6887123293",
                "Fwd IAT Max": "1805015.0",
                "Fwd IAT Min": "167.0",
                "Fwd Pkts/s": "7.295850774190399",
                "SYN Flag Cnt": "1",
                "RST Flag Cnt": "0",
                "PSH Flag Cnt": "0",
                "ACK Flag Cnt": "0",
                "CWE Flag Count": "0",
                "ECE Flag Cnt": "0"
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