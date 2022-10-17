from flask import Flask, request
from flask_cors import CORS
import json
import sys
from tensorflow import keras
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
def welcome():
    return "Python Flask for DDoS IA is Online"


@app.route("/IA", methods=["POST"])
def read():
    try:
        data = json.loads(request.get_data())
        print(data)
        testpd = pd.json_normalize(data).astype('float')
        testepdColumnsTypes = {"SrcPort": "int", "DstPort": "int", "TotFwdPkts": "int", "FwdPktLenMax": "float", "FwdPktLenMin": "float", "FwdPktLenMean": "float", "FwdPktLenStd": "float", "FlowIATMean": "float", "FlowIATStd": "float", "FlowIATMax": "float", "FlowIATMin": "float", "FwdIATTot": "float", "FwdIATMean": "float", "FwdIATStd": "float", "FwdIATMax": "float", "FwdIATMin": "float", "FwdPktss": "float", "SYNFlagCnt": "int", "RSTFlagCnt": "int", "PSHFlagCnt": "int", "ACKFlagCnt": "int", "CWEFlagCount": "int", "ECEFlagCnt": "int"} 
        for item in testpd.columns:
            if testepdColumnsTypes[item] == "int":
                testpd[item] = testpd[item].astype(int)
            else:
                testpd[item] = testpd[item].astype(float)
                
        model = keras.models.load_model('./AIV2.h5')
        predict = model.predict(testpd)
        return str(predict)
    except:
        print("An exception occurred: ", sys.exc_info()[0])
        return str(sys.exc_info()[0])