#!/usr/bin/env python3
""" 12-main """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    all_logs = collection.count_documents({})
    print(f'{all_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{count} status check')
