import json
from warnings import warn


def dumpDataToJson(data:dict,fileLocation:str) -> bool:
    if type(data) is not dict:
        warn("Data type must be 'dict'. Since it wasn't in dict format, it is stored as: {'non-dict-data':str(data)}")
        data = {'non-dict-data':str(data)}
        try:
            with open(fileLocation, 'w') as f:
                json.dump(data, f)
                return True
        except Exception as e:
            warn(e)
            return False
    else:
        try:
            with open(fileLocation, 'w') as f:
                json.dump(data, f)
                return True
        except Exception as e:
            warn(e)
            return False

def updateKeyValuePairInJson(key:str,value:str,fileLocation:str) -> bool:
    try:
        with open(fileLocation, 'r') as f:
            data = json.load(f)
            data[key] = value
            with open(fileLocation, 'w') as f:
                json.dump(data, f)
                return True
    except Exception as e:
        warn(e)
        return False

def readJsonByKey(key:str,fileLocation:str) -> str:
    with open(fileLocation, 'r') as f:
        data = json.load(f)
        return data[key]

def readWholeJson(fileLocation:str) -> dict:
    with open(fileLocation, 'r') as f:
        data = json.load(f)
        return data
