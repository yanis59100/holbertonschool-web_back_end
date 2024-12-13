#!/usr/bin/env python3
'''10-main'''


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based on its name."""
    mongo_collection.update_many({"name": name},{"$set": {"topics": topics}})
