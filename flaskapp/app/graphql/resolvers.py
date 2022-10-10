import json
from pprint import pp
from . import query
import random

random_instance = random.Random(500)


@query.field("cid10")
def fixtures(*_):
    return []
