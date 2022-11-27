import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_path = "/config/workspace/aps_failure_training_set1.csv"
Database_name = "aps_fault_detection"
collection = "sensor"

if __name__=="__main__":
    df=pd.read_csv(data_path)
    print(f"Rows and columns : {df.shape}")

    #conver data to json frame to dump data in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    #insert converted json data into mongodb
    client[Database_name][collection].insert_many(json_record)
    print(client)
 


