#!/usr/bin/env python3


def list_all(mongo_collection):
    '''Return an empty list if no document in the collection'''
    result = mongo_collection.school.find()
    if result:
        return result
    return []
