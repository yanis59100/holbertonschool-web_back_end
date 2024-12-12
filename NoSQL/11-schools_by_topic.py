#!/usr/bin/env python3
""" 11-main """


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools having a specific topic."""
    return mongo_collection.find({"topics": topic})
