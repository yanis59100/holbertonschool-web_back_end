#!/usr/bin/env python3
'''momgo collection'''


def list_all(mongo_collection):
    '''Return an empty list if no document in the collection'''
    result = mongo_collection.find()
    if result == 0:
        return []
    return list(result)
