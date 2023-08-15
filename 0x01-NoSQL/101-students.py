#!/usr/bin/env python3
""" Python function that returns all students sorted by average score """

from pymongo.collection import Collection
from typing import List


def top_students(mongo_collection: Collection) -> list:
    """ get the top students

    Args:
        mongo_collection (Collection): mongodb collection

    Returns:
        list: list of documents
    """
    # set the aggregrate pipeline, i.e arrays of stages
    pipeline: List[dict] = [
        # project stage
        {"$project": {"name": "$name",
                      "averageScore": {"$avg": "$topics.score"}}},
        # sort stage
        {"$sort": {"averageScore": -1}}


    ]
    result: list = list(mongo_collection.aggregate(pipeline))

    return result
