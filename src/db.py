import pymongo


def connectDB():
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    axpertDB = client["AxpertDB"]

    qpigs_collection = axpertDB["QPIGS"]


qpigs_dict = {"Grid_Voltage": "255.00",
              "Grid_Frequency": "50.00", "Battery_Capacity": "90%"}

x = qpigs_collection.insert_one(qpigs_dict)
print(client.list_database_names())
print(x.inserted_id)
